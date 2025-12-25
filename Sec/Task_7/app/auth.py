from fastapi import HTTPException, Header, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_session
from .models import User, Token

async def get_user_by_token(
    authorization: str | None = Header(None),
    session: AsyncSession = Depends(get_session)
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    if not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header")
    
    token_value = authorization[7:]
    
    stmt = (
        select(User)
        .join(Token, Token.user_id == User.id)
        .where(Token.value == token_value)
        .where(Token.is_valid == True)
    )
    
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return {"id": user.id, "name": user.name}