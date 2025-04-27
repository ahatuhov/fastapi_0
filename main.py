from fastapi import FastAPI, Body, Path
import uvicorn
from pydantic import BaseModel, EmailStr
from typing import Annotated

app = FastAPI()


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


@app.get("/items/")
def get_items_list():
    return [
        "item_1",
        "item_2",
        "item_3",
        "item_4",
        "item_5",
    ]


# Более часный запрос
@app.get("/items/latest/")
def get_item_latest():  # <--- должен быть написан раньше чем 'get_item_by_id' т.к. это более общий запрос
    return {
        "item": {
            "id": 0,
            "name": "Latest"
        }
    }


# При написании запросов учитывается правило "От часного к общему"
# Т.е. сначала пише более часные запросы потом более общие запросы
# Если более часные запросы писать после общих запросов, то часные запросы работать не будут

# Более общий запрос
@app.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):  # указываем строго тип (int) для item_id
    return {
        "item": {
            "id": item_id
        }
    }


if __name__ == '__main__':
    # для автоматического перезапуска приложения
    uvicorn.run("main:app", reload=True)
