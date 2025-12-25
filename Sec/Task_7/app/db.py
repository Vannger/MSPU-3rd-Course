import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

engine = None
async_session_factory = None

class Base(DeclarativeBase):
    pass

async def init_db():
    global engine, async_session_factory
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not found")
    
    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def close_db():
    global engine, async_session_factory
    if engine:
        await engine.dispose()
    engine = None
    async_session_factory = None

async def get_session() -> AsyncSession:
    if async_session_factory is None:
        await init_db()
        
    async with async_session_factory() as session:
        yield session