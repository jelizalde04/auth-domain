from sqlalchemy.orm import Session
from models.Responsible import Responsible

def authenticate_responsible(db: Session, email: str, password: str):
    print(f"Searching for responsible with email: {email}")  
    responsible = db.query(Responsible).filter(Responsible.email == email).first()

    print(f"Responsible found: {responsible}")  

    if not responsible:
        return None  

    if password.strip() != responsible.password.strip():
        print(f"Incorrect password for email: {email}")  
        return None  

    return responsible  
