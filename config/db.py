from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError

# Load environment variables from the .env file
load_dotenv()

# Retrieve the database connection details from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construct the connection URL for the database
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the SQLAlchemy engine with the connection URL
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the base class for ORM models
Base = declarative_base()

# Attempt to connect to the database to ensure the connection is working
try:
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except OperationalError as e:
    print(f"Error connecting to the database: {e}")
