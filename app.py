"""FastAPI квадратного уравнения"""
from fastapi import FastAPI
app = FastAPI()


@app.get("/kvyr")
def kvyr(a: float, b: float, c: float):
    """функция выводит a, b, c"""
    return {
        "a": a,
        "b": b,
        "c": c
     }
