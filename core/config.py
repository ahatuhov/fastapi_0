from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"  # указываем путь к БД
    # db_echo: bool = False  # для Прода
    db_echo: bool = (
        True  # только для режима отладки. (!!!) Обязательно закомментировать для прода
    )


settings = Setting()  # инициализируем доступ к переменным окружения
