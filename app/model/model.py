# python.
import typing

# 3rd.
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import backref
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

# local.
from app import constants
from app.model.exceptions import EmailAlreadyRegistered
from app.model.exceptions import MissingField
from app.model.exceptions import UsernameAlreadyRegistered


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    iduser = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    password = Column(String(50), nullable=False)


class Todo(Base):
    __tablename__ = 'todo'
    idtodo = Column(Integer(), primary_key=True)
    description = Column(String(127), nullable=False)
    is_completed = Column(Boolean(), default=False)
    id_user = Column(Integer(), ForeignKey('user.iduser'))
    user = relationship('User', backref=backref('todos'))


class Model(object):
    def __init__(self) -> None:
        """Manage the models."""
        self.engine = create_engine(f'sqlite:///{constants.DB_NAME}')
        Base.metadata.create_all(bind=self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self._create_default_user()

    def _create_default_user(self) -> None:
        if not self.select_user(username='admin'):
            user = User(
                username=constants.DEFAULT_USERNAME,
                password=constants.DEFAULT_PASSWORD,
            )
            self.insert_user(user)

    def insert_user(self, user: User) -> None:
        if user.username is None or user.password is None:
            raise MissingField('username, password are required fields.')

        if user.username is not None and self.select_user(
            username=user.username
        ):
            raise UsernameAlreadyRegistered(
                'The username {user.username} already registered.'
            )

        if user.email is not None and self.select_user(email=user.email):
            raise EmailAlreadyRegistered(
                f'The email {user.email} already registered.'
            )

        self.session.add(user)
        self.session.commit()

    def select_users(self) -> typing.List[User]:
        return self.session.query(User).all()

    def select_user(self, **values) -> User:
        return self.session.query(User).filter_by(**values).first()

    def update_user(self, user: User) -> None:
        if user.username is None or user.password is None:
            raise MissingField('username, password are required fields.')

        self.session.commit()

    def delete_user(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()

    def insert_todo(self, todo: Todo) -> None:
        if todo.description is None or todo.user is None:
            raise MissingField('description, user are required fields.')

        self.session.add(todo)
        self.session.commit()

    def select_todos(self, **values) -> typing.List[Todo]:
        return self.session.query(Todo).filter_by(**values).all()

    def select_todo(self, **values) -> Todo:
        return self.session.query(Todo).filter_by(**values).first()

    def update_todo(self, todo: Todo) -> None:
        if todo.description is None or todo.user is None:
            raise MissingField('description, user are required fields.')

        self.session.commit()

    def delete_todo(self, todo: Todo) -> None:
        self.session.delete(todo)
        self.session.commit()
