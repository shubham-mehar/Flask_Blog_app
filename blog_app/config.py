import os


class Config():
    SQLALCHEMY_DATABASE_URI  = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY  = os.environ.get('SECRET_KEY')
    MAIL_SERVER ='smtp.google.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASS = os.environ.get('EMAIL_PASS')