from .session import engine, SQLModel


def init_db():
    SQLModel.metadata.create_all(engine)
