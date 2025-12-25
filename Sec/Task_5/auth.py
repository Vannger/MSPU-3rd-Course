import hashlib
import time
from validation import validate_password
from user import User, UserStorage
from argon2 import PasswordHasher


MAX_ATTEMPTS = 5

def register_user(storage: UserStorage, username: str, email: str, password: str) -> User:
    """
    Создает пользователя и сохраняет хэш пароля в виде Argon2.
    """
    if User.exists(storage, username):
        raise ValueError("Пользователь с таким username уже существует")

    validate_password(password)

    ph = PasswordHasher()
    argon_hash =  ph.hash(password.encode("utf-8"))
    user = User(username=username, email=email, password_hash=argon_hash, 
                is_account_locked=False)
    user.save(storage)
    return user

def is_account_locked(storage: UserStorage, username: str):
    user = User.load(storage, username)
    if user is None:
        return False
    
    return user.is_account_locked


def verify_credentials(storage: UserStorage, username: str, password: str) -> bool:
    """
    Возвращает True, если пользователь существует и argon2(password) совпадает с сохраненным.
    """
    user = User.load(storage, username)
    if user is None:
        return False
    
    if user.is_account_locked:
        return False
    
    ph = PasswordHasher()
    argon_hash =  ph.hash(password.encode("utf-8"))
    md5_hex = hashlib.md5(password.encode("utf-8")).hexdigest()
    if user.password_hash == md5_hex:
        user.password_hash = argon_hash
        user.save(storage)
    
    if user.password_hash == argon_hash:
        user.attempts=0
        user.save(storage)
    else:
        user.attempts+=1
        user.save(storage)
    
    if user.attempts==MAX_ATTEMPTS:
        user.is_account_locked=True
        user.save(storage)
        return False

    return user.password_hash == argon_hash
