from pydantic import BaseModel

# Este modelo en la v 3.10 de python da problemas
# class User(BaseModel):
#     id: str | None = None
#     username: str
#     email: str

# Se corrige 
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    username: str
    email: str