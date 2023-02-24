import os
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.environ.get("DEBUG_MODE", False)
DJANGO_SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")

# Postgres
DB_ENGINE = os.environ.get("DB_ENGINE", "django.db.backends.mysql")
DB_NAME = os.environ.get("DB_NAME", "taxila")
DB_USERNAME = os.environ.get("DB_USERNAME", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "127.0.0.1")
DB_PORT = os.environ.get("DB_PORT", "3306")

# Redis
REDIS_URL = os.environ.get("REDIS_URL", "127.0.0.1")
REDIS_USERNAME = os.environ.get("REDIS_USERNAME", "default")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "password")

# AWS
AWS_IAM_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_IAM_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_S3_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
