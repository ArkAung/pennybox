from pennybox.services.expense_service import ExpenseService
from pennybox.models.expense import User, Expense

def test_get_or_create_user(db_session):
    telegram_id = "u123456"
    user = ExpenseService.get_or_create_user(db_session, telegram_id)
    assert user.telegram_id == telegram_id
    
    # Test getting existing user
    same_user = ExpenseService.get_or_create_user(db_session, telegram_id)
    assert same_user.id == user.id

def test_add_expenses(db_session):
    telegram_id = 123456
    expenses = [
        {"amount": 10.0, "item": "Coffee", "category": "Food"},
        {"amount": 20.0, "item": "Book", "category": "Entertainment"}
    ]
    
    db_expenses = ExpenseService.add_expenses(db_session, telegram_id, expenses)
    assert len(db_expenses) == 2
    assert db_expenses[0].amount == 10.0
    assert db_expenses[1].item == "Book"