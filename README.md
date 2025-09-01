# Online Library API

This is a complex online library backend built with FastAPI. It is designed for testing and benchmarking code documentation software.

## Features

- User registration and JWT authentication
- Two user roles: `MEMBER` and `LIBRARIAN`
- Full CRUD operations for books (Librarian only)
- Book borrowing and returning
- Book reservations for unavailable books
- Calculation of fines for overdue books

## Setup and Installation

1.  **Clone the repository (or download the source code).**

2.  **Install dependencies:**
    Open your terminal in the project root and run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

## API Documentation

Once the server is running, the interactive API documentation (Swagger UI) will be available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
