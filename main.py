from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Calculator")


@app.get("/")
def home():
    return {"message": "API Calculator is running"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")

    return {"result": a / b}


@app.get("/power")
def power(a: float, b: float):
    return {"result": a ** b}