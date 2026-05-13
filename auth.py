from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):

    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )   

def create_access_token(data: dict):

    encoding_data = data.copy()
    expire_at = datetime.now(timezone.utc) + timedelta(hours=1)

    encoding_data.update({"exp": expire_at})

    token = jwt.encode(
        encoding_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

def verify_token(token: str):

    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload
    
    except JWTError:
        return None