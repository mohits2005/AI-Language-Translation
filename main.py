from fastapi import FastAPI
from schemas import TranslationRequest
from translate import translate_text, get_supported_languages

from database import Base, engine,SessionLocal
from models import TranslationLog, User

from schemas import UserRegister, UserLogin
from auth import hash_password, verify_password

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from auth import hash_password, verify_password, create_access_token, verify_token

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse

from fastapi.responses import FileResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

app = FastAPI(
    title="AI Translation API",
    description="Translate text between languages using NLP models",
    version="1.0.0"
)

security = HTTPBearer(
    bearerFormat="JWT"
)

limiter = Limiter(
    key_func=get_remote_address
)

app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)
@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "message": "Something went wrong",
            "error": str(exc)
        }
    )
Base.metadata.create_all(bind=engine)

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    payload = verify_token(token)

    if payload is None:

        return {
            "message": "Invalid token"
        }

    return payload

@app.get("/")
def home():
    return {
        "message": "AI Translation API Running"
    }

@app.get("/languages")
def supported_languages():

    languages = get_supported_languages()

    return {
        "languages": languages
    }

@app.post("/translate")

@limiter.limit("5/minute")

def translate(request: Request, req: TranslationRequest, user=Depends(get_current_user)):

    #translated = translate_text(req.text, req.source_lang, req.target_lang)
    try:

        translated = translate_text(
        req.text,
        req.source_lang,
        req.target_lang
    )

    except Exception:

        return {
            "message": "Translation failed"
        }

    db = SessionLocal()

    log = TranslationLog(
        user_id=user["user_id"],
        original_text = req.text,
        translated_text = translated,
        source_language = req.source_lang,
        target_language = req.target_lang
    )

    db.add(log)
    db.commit()
    db.refresh(log)
    db.close()

    return {
        "original_text": req.text,
        "translated_text": translated,
        "source_language": req.source_lang,
        "target_language": req.target_lang
    }

@app.get("/history")
def get_history(user=Depends(get_current_user)):

    db = SessionLocal()

    logs = db.query(TranslationLog).filter(
    TranslationLog.user_id == user["user_id"]).all()
    
    db.close()

    return logs

@app.post("/register")
def register(user: UserRegister):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        db.close()

        return {
            "Message": "Email Already Exists"
        }
    
    hashed_password = hash_password(user.password)

    new_user = User(
        username = user.username,
        email = user.email,
        password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {
        "Message": "User Registered Succesfully"
    }

@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        db.close()

        return {
            "Message": "Invalid Email"
        }
    
    valid_password = verify_password(
        user.password, existing_user.password
    )

    if not valid_password:
        db.close()

        return {
            "Message": "Invalid Password"
        }
    token = create_access_token(
        {
            "user_id": existing_user.id,
            "email": existing_user.email
        }
    )
    
    db.close()

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    

@app.get("/export-history")
def export_history(
    user=Depends(get_current_user)
):

    db = SessionLocal()

    logs = db.query(TranslationLog).filter(
        TranslationLog.user_id == user["user_id"]
    ).all()

    db.close()

    filename = f"translation_history_user_{user['user_id']}.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Translation History",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    for log in logs:
        text = f"""
        <b>Original:</b> {log.original_text}<br/>
        <b>Translated:</b> {log.translated_text}<br/>
        <b>From:</b> {log.source_language}<br/>
        <b>To:</b> {log.target_language}<br/>
        <b>Date:</b> {log.created_at}<br/><br/>
        """

        paragraph = Paragraph(
            text,
            styles['BodyText']
        )

        elements.append(paragraph)

        elements.append(Spacer(1, 12))
    
    doc.build(elements)

    return FileResponse(
        path=filename,
        filename=filename,
        media_type='application/pdf'
    )

