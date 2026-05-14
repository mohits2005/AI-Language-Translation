AI Language Translation API

This is an intelligence powered multilingual translation backend built using FastAPI and MySQL and JWT Authentication.

This project provides scalable translation APIs that can translate text between multiple languages.

It also maintains user authentication, translation history, PDF export functionality, rate limiting and detailed API documentation.

Features

Authentication and Security

* User Registration and Login
* JWT Token Authentication
* Password Hashing using Bcrypt
* API Routes
* API Rate Limiting

Translation Features

* Multilingual Text Translation
* Dynamic Supported Languages Endpoint
* User-specific Translation History
* Translation Logging

* PDF Export of Translation History

Backend Features

* FastAPI REST APIs
* MySQL Database Integration
* SQLAlchemy ORM
* Global Exception Handling
* Swagger API Documentation
* Modular Backend Architecture
Technologies Used
FastAPI is the Backend API Framework
MySQL is used for Database Management
SQLAlchemy is the ORM for Database Operations
JWT is used for Authentication and Authorization
Deep Translator is the NLP Translation Service
Passlib plus Bcrypt is used for Password Hashing
SlowAPI is used for Rate Limiting
ReportLab is used for PDF Export
Python is the Core Programming Language

Project Structure

AI Translation Model has the following files

* auth.py
* config.py
* database.py
* main.py
* models.py
* schemas.py
* translate.py
* requirements.txt
*.gitignore
*.env

Installation and Setup

1. Clone the Repository using git clone https://github.com/mohits2005/AI-Language-Translation.git

2. Move into the Project Folder using cd AI-Language-Translation

3. Install Dependencies using pip install -r requirements.txt

4. Configure Environment Variables by creating a.env file with the following

DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/translation_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

5. Run the Server using python -m main:app --reload

API Documentation

After running the server you can access the Swagger Docs at http://127.0.0.1:8000/docs

Main API Endpoints

* /register is a POST endpoint to Register New User

* /login is a POST endpoint to Login User and Generate JWT

* /translate is a POST endpoint to Translate Text

* /history is a GET endpoint to Get User Translation History

* /languages is a GET endpoint to Get Supported Languages

* /export-history is a GET endpoint to Export Translation History as PDF

Authentication Flow

1. User Registers

2. User Logs In

3. JWT Token is Generated

4. User Authorizes, via Swagger or UI

5. Protected APIs become

Database Design

Users Table Stores the following information

* Username

* Email

* Hashed Password

Translation Logs Table Stores the following information

* Text

* Translated Text

* Source Language

* Target Language

* Translation Timestamp

* User ID

PDF Export Feature

Users can export their personal translation history as a PDF report.

This feature improves usability and reporting and offline access.

Error Handling

The following error handling is implemented

* Global Exception Handling

* Invalid Token Handling

* Translation Failure Handling

* Rate Limit Exceeded Handling

Future Enhancements

* Frontend UI Integration

* Cloud Deployment

* Translation Analytics Dashboard

* Voice Translation

* OCR Text Translation

* Real-time Chat Translation
