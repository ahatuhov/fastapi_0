from fastapi import FastAPI
import uvicorn
from items_views import router as items_router
from users.views import router as user_router

app = FastAPI()
app.include_router(
    items_router
)  # регистрируем в (app) пространство имен в виде нового роутера
app.include_router(user_router)  # регистрируем в (app) пакет для users


@app.get("/")
def hello():
    return {
        "message": "Hello!",
    }


# Запрос с query-параметрами
@app.get("/hello/")
def say_hello(
    name: str = "World",
):  # для параметра 'name' значение по умолчанию равно "World"
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    # для автоматического перезапуска приложения
    uvicorn.run("main:app", reload=True)
