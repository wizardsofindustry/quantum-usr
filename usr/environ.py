"""Environment variables specified by the application Quantumfile."""
import os

SECRET_KEY = os.getenv('USR_SECRET_KEY')
RDBMS_DSN = os.getenv('USR_RDBMS_DSN')
HTTP_ADDR = os.getenv('USR_HTTP_ADDR')
HTTP_PORT = os.getenv('USR_HTTP_PORT')
