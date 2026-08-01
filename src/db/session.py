from contextlib import contextmanager

from sqlalchemy.orm import Session, sessionmaker

from .engine import engine

__sessionmaker = sessionmaker(engine, expire_on_commit=False, class_=Session)

@contextmanager
def get_session():
    with __sessionmaker() as session:
        yield session
