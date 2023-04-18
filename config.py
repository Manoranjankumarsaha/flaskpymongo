import os
import secrets
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



class Config(object):
    DEBUG = True
    SECRET_KEY=os.environ.get('SECRET_KET') or secrets.token_hex(16)
    JWT_SECRET_KEY = secrets.token_urlsafe(32)
    
    MONGODB_SETTINGS = [{"db": "mktest", "host": "127.0.0.1", "port": 27017, "username": "root", "password": "mongo#Root053", "alias": "default"}]
    
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'MAIL_USERNAME'
    MAIL_PASSWORD = 'MAIL_PASSWORD'
    MAIL_DEFAULT_SENDER = 'from@example.com'
    
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = 'your_email_address@gmail.com'
    # MAIL_PASSWORD = 'your_email_password'
    # MAIL_DEFAULT_SENDER = 'your_email_address@gmail.com' #optional