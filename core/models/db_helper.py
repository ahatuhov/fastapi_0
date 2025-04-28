from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(  # создаем новый движок
            url=url,
            echo=echo,
        )

        # создаем фабрику для сессий
        self.session_factory = async_sessionmaker(  # создаем сессию на базе асинхронного async_sessionmaker
            bind=self.engine,  # передаем движок
            autoflush=False,  # убираем автоматическую подготовку к коммиту
            autocommit=False,  # выключаем автокоммит
            expire_on_commit=False,  # отключаем автоматическое удаление информации из сессии
        )


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
