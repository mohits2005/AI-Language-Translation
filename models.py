from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from datetime import datetime, timezone
from database import Base
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    email = Column(String(200), unique=True)
    password = Column(String(255))
    translations = relationship("TranslationLog", backref="user")    

class TranslationLog(Base):

    __tablename__ = "translation_logs"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(String(1000))
    translated_text = Column(String(1000))
    source_language = Column(String(20))
    target_language = Column(String(20))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user_id = Column(Integer, ForeignKey("users.id"))
    