from os.path import defpath

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class OrmCategory(Base):
    __tablename__ = 'orm_category'
    id = sa.Column(
        sa.Integer,
        primary_key=True
    )
    name = sa.Column(
        sa.String(255),
        nullable=False,
        unique=True,
        index=True
    )
    products = relationship(
        "OrmProduct",
        back_populates="category"
    )


class OrmProduct(Base):
    __tablename__ = 'products'
    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True
    )
    created_at = sa.Column(
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),
        index=True
    )
    updated_at = sa.Column(
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),
        index=True
    )
    deleted_at = sa.Column(
        sa.DateTime,
        nullable=True
    )
    name = sa.Column(
        sa.String(255),
        nullable=False,
        unique=True
    )
    price = sa.Column(
        sa.Numeric,
        nullable=False
    )
    is_active = sa.Column(
        sa.Boolean,
        nullable=False,
        default=True
    )
    category_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('orm_category.id')
    )
    category = relationship(
        "OrmCategory",
        back_populates="products",
    )
