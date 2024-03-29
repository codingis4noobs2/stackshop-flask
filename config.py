from dotenv import load_dotenv
import os

load_dotenv()

PROVIDER_CLIENT_ID = os.getenv('PROVIDER_CLIENT_ID')
PROVIDER_CLIENT_SECRET = os.getenv('PROVIDER_CLIENT_SECRET')
PROVIDER_ISSUER = os.getenv('PROVIDER_ISSUER')
FLASK_SECRET = os.getenv('FLASK_SECRET')