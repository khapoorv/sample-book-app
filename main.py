
from fastapi import FastAPI
from .api import users, books, admin

app = FastAPI(
    title="Online Library API",
    description="A complex API for managing an online library, built with FastAPI.",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Online Library API"}
