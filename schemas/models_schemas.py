from pydantic import BaseModel


class RoleSchema(BaseModel):
    role_name: str


class UserSchema(BaseModel):
    telegram_id: int
    username: str
    password: str
    role_id: int


class GetUserSchema(BaseModel):
    telegram_id: int
    username: str
    role_id: str