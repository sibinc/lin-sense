import os
import mysql.connector
import redis
from dotenv import load_dotenv
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env from the project root
load_dotenv(BASE_DIR / ".env")

# Database Configuration
db_config = {
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'host': os.getenv('DATABASE_HOST'),
    'database': os.getenv('DATABASE_NAME')
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Redis Configuration
cache = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT')),
    password=os.getenv('REDIS_PASSWORD'),
    db=0
)
