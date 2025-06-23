swagger_docs = {
    "openapi": "3.0.2",
    "info": {
        "title": "API de Login de Responsables",
        "version": "1.0.0",
        "description": "Microservicio para login y generación de JWT usando FastAPI."
    },
    "paths": {
        "/auth/login": {
            "post": {
                "summary": "Login de responsables",
                "tags": ["Auth"],
                "description": "Inicia sesión y retorna un JWT con el ID del responsable.",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "email": {"type": "string", "example": "usuario@correo.com"},
                                    "password": {"type": "string", "example": "mi_contraseña123"}
                                },
                                "required": ["email", "password"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Login exitoso",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "token": {"type": "string"},
                                        "responsibleId": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "401": {"description": "Credenciales inválidas"}
                }
            }
        }
    },
    "tags": [
        {"name": "Auth", "description": "Endpoints para autenticación"}
    ]
}
