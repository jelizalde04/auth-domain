from sqlalchemy.orm import Session
from models.Responsible import Responsible

def authenticate_responsible(db: Session, email: str, password: str):
    print(f"Searching for responsible with email: {email}")  # Debugging: print the email being searched
    responsible = db.query(Responsible).filter(Responsible.email == email).first()

    # Debugging: check if the responsible was found
    print(f"Responsible found: {responsible}")  # Check if the responsible was found in the database

    if not responsible:
        return None  # Return None if no responsible was found with the provided email

    if password.strip() != responsible.password.strip():
        print(f"Incorrect password for email: {email}")  # Debugging: print message for incorrect password
        return None  # Return None if the password does not match

    return responsible  # Return the responsible if authentication is successful
