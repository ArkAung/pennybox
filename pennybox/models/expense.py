from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)
    expenses = relationship("Expense", back_populates="user")
    created_at = Column(DateTime, default=func.now())

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    item = Column(String, nullable=False)
    category = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="expenses")
    created_at = Column(DateTime, default=func.now())