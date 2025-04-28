from .base import Base
from sqlalchemy.orm import Mapped


class Product(Base):
    __tablename__ = "Products"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]


# Как все выглядит после работы с моделью

# CREATE TABLE "Products" (
# 	name VARCHAR NOT NULL,
# 	description VARCHAR NOT NULL,
# 	price INTEGER NOT NULL,
# 	id INTEGER NOT NULL,
# 	PRIMARY KEY (id)
# )
