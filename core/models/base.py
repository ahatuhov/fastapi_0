from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    __abstract__ = (
        True  # говорит о том что эта таблица абстрактная и ее не нужно создавать в БД
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"  # тут мы автоматически генерируем имя таблицы

    id: Mapped[int] = mapped_column(primary_key=True)
