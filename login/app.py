import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import Base, engine
from routes.authRoutes import router as auth_router
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError

# Configure logging to display in the console
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Get the environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Build the database connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the engine with the connection URL
engine = create_engine(DATABASE_URL, echo=True)

# Create the database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for tables
Base = declarative_base()

# Attempt to connect to the database to verify the connection
try:
    with engine.connect() as connection:
        logger.info("Successful connection to the database!")
except OperationalError as e:
    logger.error(f"Error connecting to the database: {e}")

# Create the FastAPI app
app = FastAPI(docs_url="/api-docs-login")

# Add CORS middleware for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],           # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],           # Allow all headers
)

# Create the tables if they do not exist
Base.metadata.create_all(bind=engine)

# Include the authentication routes
app.include_router(auth_router, prefix="/auth")

@app.get("/health", tags=["Health Check"])
def simple_health_check():
    return {"status": "ok"}

# Configure server execution with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1001)
