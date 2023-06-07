import os
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.environ.get("DEBUG_MODE", False)
DJANGO_SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")

# Postgres
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USERNAME = os.environ.get("DB_USERNAME", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "postgres")
DB_PORT = os.environ.get("DB_PORT", "5432")

# AWS
AWS_IAM_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_IAM_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_S3_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")

# Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

MEILISEARCH_URL = os.environ.get("MEILISEARCH_URL", "127.0.0.1:7700")
