from daos.user_dao import UserDAO
from models.user import User
import time

dao = UserDAO()

def test_user_select():
    user_list = dao.select_all()
    assert len(user_list) >= 3

def test_user_insert():
    user = User(None, 'Joanne Test', 'joannetest@example.com')
    dao.insert(user)
    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails

def test_user_update():
    user = User(None, 'Joe Test', 'testttt@example.com')
    assigned_id = dao.insert(user)

    corrected_email = 'joetest@example.com'
    user.id = assigned_id
    user.email = corrected_email
    dao.update(user)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails

    # cleanup
    dao.delete(assigned_id)

def test_user_delete():
    user = User(None, 'Joe Test', 'joetest@example.com')
    assigned_id = dao.insert(user)
    dao.delete(assigned_id)

    new_dao = UserDAO()
    user_list = new_dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails