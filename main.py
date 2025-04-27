from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr
from items_views import router as items_router

app = FastAPI()
app.include_router(items_router)  # регистрируем в (app) пространство имен в виде нового роутера


# создали специальный класс для волидации данных в запросе
class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello():
    return {
        "message": "Hello!",
    }


# Запрос с query-параметрами
@app.get("/hello/")
def say_hello(name: str = "World"):  # для параметра 'name' значение по умолчанию равно "World"
    name = name.strip().title()
    return {
        "message": f"Hello {name}!"
    }


@app.post("/users/")
# def create_user(email: EmailStr = Body()):  # тут показываем что 'email' будет передаваться в body
def create_user(user: CreateUser):  # также передаем данные в 'body' но уже с помощью класса 'CreateUser'
    return {
        "message": "success",
        "email": user.email,
    }


@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == '__main__':
    # для автоматического перезапуска приложения
    uvicorn.run("main:app", reload=True)
