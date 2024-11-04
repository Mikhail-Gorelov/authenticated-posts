# FastAPI JWT Auth Example

This project is a simple FastAPI application demonstrating JWT-based authentication. It includes endpoints for managing posts with secure access for authenticated users.

## Features

- JWT-based authentication
- Create, read posts
- Secure endpoints accessible only to authenticated users

## Requirements

- Python 3.12 or higher
- pip

## Installation

1. **Clone the repository:**
```shell
git clone git@github.com:Mikhail-Gorelov/authenticated-posts.git
cd /authenticated-posts
```

2. **Create a virtual environment:**
```shell
python -m venv venv
```

3. **Activate the virtual environment:**
```shell
source venv/bin/activate
```

4. **Running the application:**
```shell
uvicorn app.main:app --reload
```
You can access the documentation for all endpoints at the /docs URL.

5. **Authentication:**
There is only one user established for the application. See the example below:

```http
POST /sign-in
Content-Type: application/json

{
    "username": "user",
    "password": "pass"
}