from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session
