Создание новой миграции
alembic revision --autogenerate -m "migration comment"

Накат всех миграций
alembic upgrade head

Откат миграции
alembic downgrade -1 (ну или сколько надо)
