from pydantic import BaseModel
import sqlalchemy

class Role(BaseModel):
    id: int
    role_name: str


class User(BaseModel):
    id: int
    telegram_id: int
    username: str
    role: Role