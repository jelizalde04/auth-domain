from fastapi import HTTPException
from services.AuthService import authenticate_responsible
from utils.jwt_utils import create_access_token
from config.db import SessionLocal

def login_controller(login_req):
    db = SessionLocal()  
    responsible = authenticate_responsible(db, login_req.email, login_req.password)  
    
   
    if not responsible:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
 
    token = create_access_token({"userId": str(responsible.id)}) 
    
   
    return {"token": token}
