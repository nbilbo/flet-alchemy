from typing import List
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from flet_alchemy.config import settings

current_id_user: Optional[int] = None


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    todos: Mapped[List['Todo']] = relationship(back_populates='user')


class Todo(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    completed: Mapped[bool]

    id_user: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='todos')


def get_session() -> Session:
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        return session


def get_current_id_user() -> int:
    return current_id_user


def set_current_id_user(id_user: int) -> None:
    global current_id_user
    current_id_user = id_user
