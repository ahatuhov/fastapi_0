from users.schemas import CreateUser
from fastapi import Path, APIRouter
from users.crud import create_user


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
# def create_user(email: EmailStr = Body()):  # тут показываем что 'email' будет передаваться в body
def create_user_view(user: CreateUser):  # также передаем данные в 'body' но уже с помощью класса 'CreateUser'
    return create_user(user)
