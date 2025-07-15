# 1. General Domain Overview  

The auth-domain manages user authentication within a distributed system. Its purpose is to provide secure access to resources using JWT (JSON Web Tokens). This domain handles the login process, token generation, and user credential validation.

## Microservices Involved

**Login:** This microservice allows users to log in with their credentials (email and password). Upon successful login, it generates a JWT that the user can use to authenticate future requests.

## Technologies and Tools Used

- **FastAPI:** Framework for building the API.
- **SQLAlchemy:** ORM for interacting with the PostgreSQL database.
- **PostgreSQL:** Database for storing users and their credentials.
- **JWT:** For user authentication via tokens.
- **Docker:** To containerize the application and facilitate deployment.
- **Pydantic:** For request data validation.

# 2. Folder Structure

The `auth-domain` folder is organized as follows:

```
auth-domain/
│
├── app.py                   # Main file to run the FastAPI application
├── config/                  # Configuration files for the database and other settings
│   └── db.py                # PostgreSQL database configuration
├── controllers/             # Logic for handling routes
│   └── AuthController.py    # Logic for handling user login
├── routes/                  # Files defining API routes/endpoints
│   └── authRoutes.py        # Authentication-related routes
├── services/                # Services interacting with the database
│   └── AuthService.py       # Service for user authentication
├── utils/                   # Utility functions
│   └── jwt_utils.py         # Functions for creating and verifying JWTs
├── requirements.txt         # Project dependencies
└── Dockerfile               # Docker configuration for containerizing the application
```

### Description of Important Folders

- **controllers/**: Contains the logic for handling incoming requests and generating responses.
- **routes/**: Defines the routes for the API, including authentication-related routes.
- **services/**: Contains services that interact with the database to handle complex operations.
- **utils/**: Contains utility functions, such as JWT generation.
- **config/**: Contains general configuration for the application, including database settings.

# 3. Technologies Used

- **Programming Language:** Python 3.x
- **Framework:** FastAPI
- **Database:** PostgreSQL (with SQLAlchemy as ORM)
- **Authentication:** JWT (JSON Web Tokens)
- **Containerization:** Docker for packaging the application

# 4. General Domain Workflow

The login microservice is responsible for authenticating users via their credentials (email and password). The general workflow is as follows:

1. **Login:** The user sends their credentials via a POST request to the `/auth/login` endpoint.
2. **Verification:** The `AuthService` verifies the credentials against the database.
3. **Token Generation:** If the credentials are valid, the microservice generates a JWT with an expiration time and returns it to the client.
4. **Authentication for Future Requests:** The client can use the JWT for authenticating future requests.


# 5. Authentication and Security

The domain uses JWT to authenticate users. The token is generated when a user successfully logs in and must be included in the authorization header for future requests:

```bash
Authorization: Bearer jwt_token_string
```

The service also implements CORS to allow the frontend and backend to communicate across different domains.

# 6. Swagger Documentation


FastAPI automatically generates interactive documentation using Swagger. You can access the API documentation at:

[http://localhost:1001/api-docs-login](http://localhost:1001/api-docs-login)