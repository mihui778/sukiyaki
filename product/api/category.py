from fastapi import APIRouter

from database import Session
from orm import OrmCategory
from product.domain.schemas.category import CategoryOut, CategoryIn

router = APIRouter(tags=["Category"])


@router.post("", status_code=201)
def create_category(data: CategoryIn):
    with Session() as session:
        category = OrmCategory(**data.model_dump())
        session.add(category)
        session.commit()
        session.flush()

    return CategoryOut(id=category.id, name=category.name)
