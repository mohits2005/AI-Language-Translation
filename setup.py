import pymysql
import subprocess
import sys

from sqlalchemy import create_engine
from database import Base
from models import User, TranslationLog

# ---------------- DATABASE CONFIG ---------------- #

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "YOUR_PASSWORD"
DB_NAME = "translation_db"

# ---------------- CREATE DATABASE ---------------- #

try:

    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
    )

    print("✅ Database created successfully")

    connection.close()

except Exception as e:

    print(f"❌ Database creation failed: {e}")

# ---------------- CREATE TABLES ---------------- #

try:

    DATABASE_URL = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    engine = create_engine(DATABASE_URL)

    Base.metadata.create_all(bind=engine)

    print("✅ Tables created successfully")

except Exception as e:

    print(f"❌ Table creation failed: {e}")

# ---------------- INSTALL DEPENDENCIES CHECK ---------------- #

required_packages = [
    "fastapi",
    "uvicorn",
    "sqlalchemy",
    "pymysql",
    "python-jose",
    "passlib",
    "bcrypt",
    "deep-translator",
    "streamlit",
    "reportlab",
    "slowapi",
    "cryptography"
]

print("\n📦 Checking required packages...\n")

for package in required_packages:

    try:

        __import__(package.replace("-", "_"))

        print(f"✅ {package} installed")

    except ImportError:

        print(f"⚠️ Installing {package}...")

        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package]
        )

print("\n🎉 Project setup completed successfully!")
