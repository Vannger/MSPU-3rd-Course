from fastapi import FastAPI, Depends, HTTPException, Query, Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, Any
from contextlib import asynccontextmanager
from pydantic import BaseModel
import secrets
import hashlib
from .db import get_session, init_db, close_db
from .auth import get_user_by_token
from .models import User, Token, Order, Good
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

app = FastAPI(title="SQLi Lab (ORM Fixed)", lifespan=lifespan)

class AuthRequest(BaseModel):
    name: str
    password: str

@app.post("/auth/token")
async def auth_token(
    body: AuthRequest, 
    session: AsyncSession = Depends(get_session)
):
    stmt = select(User).where(User.name == body.name)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user or not pwd_context.verify(body.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    stmt_token = select(Token).where(Token.user_id == user.id, Token.is_valid == True)
    token_result = await session.execute(stmt_token)
    token_obj = token_result.scalar_one_or_none()
    
    if not token_obj:
        token_str = secrets.token_urlsafe(64)
        new_token = Token(user_id=user.id, value=token_str)
        session.add(new_token)
        await session.commit()
        return {"token": token_str}
    else:
        return {"token": token_obj.value}

@app.get("/orders")
async def list_orders(
    user: Annotated[dict[str, Any], Depends(get_user_by_token)],
    limit: int = Query(10, ge=1), 
    offset: int = Query(0, ge=0),
    session: AsyncSession = Depends(get_session)
):
    stmt = (
        select(Order)
        .where(Order.user_id == user["id"])
        .order_by(Order.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    result = await session.execute(stmt)
    rows = result.scalars().all()
    
    return [
        {"id": r.id, "user_id": r.user_id, "created_at": r.created_at.isoformat()} 
        for r in rows
    ]

@app.get("/orders/{order_id}")
async def order_details(
    order_id: int, 
    user: Annotated[dict[str, Any], Depends(get_user_by_token)],
    session: AsyncSession = Depends(get_session)
):
    stmt = select(Order).where(Order.id == order_id, Order.user_id == user["id"])
    result = await session.execute(stmt)
    order = result.scalar_one_or_none()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    stmt_goods = select(Good).where(Good.order_id == order_id)
    goods_res = await session.execute(stmt_goods)
    goods = goods_res.scalars().all()
    
    return {
        "order": {"id": order.id, "user_id": order.user_id, "created_at": order.created_at.isoformat()},
        "goods": [{"id": g.id, "name": g.name, "count": g.count, "price": g.price} for g in goods]
    }