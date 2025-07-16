# Login Microservice
  
## 1. Microservice Overview

The login microservice allows users to authenticate into the system and obtain a JWT token for future requests. This microservice ensures that only authenticated users can access protected resources.

---

## 2. Routes and Endpoints

### **POST** `/auth/login`

**Description:** Logs in and returns a JWT with the responsible user’s ID.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "my_password123"
}
```

**Response:**
```json
{
  "token": "jwt_token_string",
  "responsibleId": "user_id"
}
```

**Response Codes:**
- `200 OK`: Login successful, token generated.
- `401 Unauthorized`: Invalid credentials.

---

## 3. Microservice Functionality

- The controller receives the user’s credentials (email and password).
- It calls the `authenticate_responsible` service to verify the credentials against the database.
- If the credentials are valid, it generates a JWT using the `create_access_token` function and returns it along with the user's ID.

**Internal Flow:**
- Credentials are validated against the PostgreSQL database using SQLAlchemy.
- The JWT is generated in the `utils/jwt_utils.py` file.

---

## 4. Technologies and Tools Used

- **FastAPI:** Framework for building the service.
- **SQLAlchemy:** ORM for interacting with the PostgreSQL database.
- **JWT:** For user authentication and authorization.

---

## 5. Authentication and Security

This microservice uses JWT to authenticate users. The JWT is generated in the login controller and returned to the client for use in subsequent requests.

---

## 6. Setup and Execution

**Install dependencies:**
```bash
pip install -r requirements.txt
```
Set up the `.env` file with the necessary environment variables.

**Run the microservice:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 1001
```

---

## 7. Swagger Documentation

The interactive Swagger documentation for testing the endpoints