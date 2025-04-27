from users.schemas import CreateUser


def create_user(user: CreateUser) -> dict:  # стрелочка говорит о том что данные возвращаются в виде словаря
    user = user.model_dump()  # с помощью метода model_dump() создаем словарь из данных
    return {
        "success": True,
        "user": user,
    }
