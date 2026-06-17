from pydantic import BaseModel


class RoleCreate(BaseModel):
    role_name: str


class UserCreate(BaseModel):
    telegram_id: int
    username: str
    role_id: int