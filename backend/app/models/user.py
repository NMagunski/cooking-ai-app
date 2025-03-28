from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    saved_recipes: list[str] = []
    created_at: datetime = datetime.now()
