from typing import List
from sqlalchemy.orm import Session
from pennybox.models.expense import User, Expense
from pennybox.database.db import get_db

class ExpenseService:
    @staticmethod
    def get_or_create_user(db: Session, telegram_id: str) -> User:
        user = db.query(User).filter(User.telegram_id == telegram_id).first()
        if not user:
            user = User(telegram_id=telegram_id)
            db.add(user)
            db.commit()
            db.refresh(user)
        return user

    @staticmethod
    def add_expenses(db: Session, telegram_id: str, expenses: List[dict]) -> List[Expense]:
        user = ExpenseService.get_or_create_user(db, telegram_id)
        db_expenses = []
        for expense_data in expenses:
            expense = Expense(
                amount=expense_data["amount"],
                item=expense_data["item"],
                category=expense_data["category"],
                user_id=user.id
            )
            db_expenses.append(expense)
        
        db.add_all(db_expenses)
        db.commit()
        for expense in db_expenses:
            db.refresh(expense)
        return db_expenses

    @staticmethod
    def get_user_expenses(db: Session, telegram_id: int) -> List[Expense]:
        user = ExpenseService.get_or_create_user(db, telegram_id)
        return db.query(Expense).filter(Expense.user_id == user.id).all()
