from pydantic import BaseModel


class AuthModelResponse(BaseModel):
    id: int
    user_token: str
    name: str
    phone: str
    login: str
    email: str
    avatar: str
    is_approved: bool
