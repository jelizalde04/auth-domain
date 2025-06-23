import os
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")  # Secret key used to sign the token
JWT_ALGORITHM = "HS256"  # Algorithm used for token signing

def create_access_token(data: dict, expires_delta: int = 3600):
    """
    Generates a JWT token.

    Parameters:
    1. `data`: A dictionary containing user data to be included in the token (e.g., `userId`).
    2. `expires_delta`: Token expiration time in seconds. Defaults to 3600 seconds (1 hour).

    Returns:
    A signed JWT token.
    """
    to_encode = data.copy()  # Create a copy of the input data
    expire = datetime.utcnow() + timedelta(seconds=expires_delta)  # Set token expiration time
    to_encode.update({"exp": expire})  # Add expiration time to the data
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)  # Sign the token
    return encoded_jwt  # Return the signed token
