from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str