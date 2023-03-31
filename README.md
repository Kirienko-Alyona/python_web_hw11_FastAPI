# python_web_hw11_FastAPI

docker run --name HW11 -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres      

poetry add fastapi
poetry add uvicorn[standard]

poetry add alembic sqlalchemy
alembic init migrations

added in file ---> env.py 

target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

alembic revision --autogenerate -m 'Init'
alembic upgrade head

uvicorn main:app --host localhost --port 8000 --reload
uvicorn main:app --reload