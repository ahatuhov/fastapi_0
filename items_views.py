from typing import Annotated

from fastapi import Path, APIRouter


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def get_items_list():
    return [
        "item_1",
        "item_2",
        "item_3",
        "item_4",
        "item_5",
    ]


# Более часный запрос
@router.get("/latest/")
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
@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):  # указываем строго тип (int) для item_id
    return {
        "item": {
            "id": item_id
        }
    }
