from pydantic import BaseModel, Field

class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

class UserRegister(BaseModel):

    username: str
    email: str
    password: str = Field(max_length=72)

class UserLogin(BaseModel):

    email: str
    password: str