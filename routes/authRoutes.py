from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field
from controllers.AuthController import login_controller

router = APIRouter()

"""
@swagger
tags:
  - name: Auth
    description: Endpoints para autenticación

@swagger
/auth/login:
  post:
    summary: Login de responsables
    tags: [Auth]
    description: Inicia sesión y retorna un JWT con el ID del responsable.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - email
              - password
            properties:
              email:
                type: string
                example: usuario@correo.com
              password:
                type: string
                example: mi_contraseña123
    responses:
      200:
        description: Login exitoso
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
                responsibleId:
                  type: string
      401:
        description: Credenciales inválidas
"""

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="usuario@correo.com")
    password: str = Field(..., example="mi_contraseña123")

@router.post("/login", tags=["Auth"])
def login(login_req: LoginRequest):
    return login_controller(login_req)

