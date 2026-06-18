from database.models import User
from schemas.models_schemas import UserSchema


def create_user(user: UserSchema):
    db_user = User(username=user.username, password=user.password, telegram_id=user.telegram_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user