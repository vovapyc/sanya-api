from passlib.context import CryptContext

from .db_models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username):
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_user(db, username, email, password):
    password = get_password_hash(password)
    db_obj = User(username=username, email=email, hashed_password=password)  # type: ignore
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
