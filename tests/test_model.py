import typing
from pytest import fixture
from pytest import mark
from pytest import raises
from app.model.exceptions import EmailAlreadyRegistered
from app.model.exceptions import MissingField
from app.model.exceptions import UsernameAlreadyRegistered
from app.model.model import Model
from app.model.model import Todo
from app.model.model import User


USERS = [
    ('Panda123', None, 'jdshfkjsd123-1312@@'),
    ('Tiger321', 'tiger@hotmail.com', 'asjd@3**--ssdf@@'),
    ('Robson2023', 'rob123son@gmail.com', 'h3h4i3jdbfkjdf**/*/'),
]

UPDATED_USERS = [
    (1, 'Panda123', 'panda@hotmail.com', 'jdshfkjsd123-1312@@'),
    (2, 'Tiger321', 'tiger321@hotmail.com', 'asjd@3**--ssdf@@'),
    (3, 'Robson2023', 'rob2023son@gmail.com', 'h3h4i3jdbfkjdf**/*/'),
]

TODOS = [
    (1, 'my first todo', True),
    (1, 'my second todo', False),
    (1, 'my third todo', False),
    (2, 'my first todo', False),
    (2, 'my second todo', False),
    (3, 'my first todo', True),
    (3, 'my second todo', True),
]


UPDATED_TODOS = [
    (1, 'my first todo', True),
    (2, 'my second todo', True),
    (3, 'my third todo', True),
    (4, 'my first todo', True),
    (5, 'my second todo', True),
    (6, 'my first todo', True),
    (7, 'my second todo', True),
]


@fixture(scope='module')
def memory_model() -> typing.Generator[Model, None, None]:
    model = Model(':memory:')
    yield model


@mark.parametrize('username, email, password', USERS)
def test_insert_user_must_persist_data(
    memory_model: Model,
    username: str,
    email: typing.Optional[str],
    password: str,
) -> None:
    user = User(username=username, email=email, password=password)
    memory_model.insert_user(user)

    assert user.iduser is not None


def test_insert_user_must_raise_missing_field(memory_model: Model) -> None:
    with raises(MissingField):
        user = User(username=None, password=None)
        memory_model.insert_user(user)


@mark.parametrize('username, email, password', USERS)
def test_insert_user_must_raise_username_already_registered(
    memory_model: Model,
    username: str,
    email: typing.Optional[str],
    password: str,
) -> None:
    with raises(UsernameAlreadyRegistered):
        user = User(username=username, email=email, password=password)
        memory_model.insert_user(user)


def test_insert_user_must_raise_email_already_registered(
    memory_model: Model,
) -> None:
    with raises(EmailAlreadyRegistered):
        user = User(username='foo', password='bar', email=USERS[1][1])
        memory_model.insert_user(user)


@mark.parametrize('iduser, description, is_completed', TODOS)
def test_insert_todo_must_persist_data(
    memory_model: Model, iduser: int, description: str, is_completed: bool
) -> None:
    user = memory_model.select_user(iduser=iduser)
    todo = Todo(description=description, is_completed=is_completed, user=user)
    memory_model.insert_todo(todo)

    assert todo.idtodo is not None


def test_insert_todo_must_raise_missing_field(memory_model: Model) -> None:
    with raises(MissingField):
        todo = Todo(description=None)
        memory_model.insert_todo(todo=todo)


def test_select_users_must_return_all_users(memory_model: Model) -> None:
    users = memory_model.select_users()

    assert len(users) == len(USERS)


@mark.parametrize('username, password', [(user[0], user[2]) for user in USERS])
def test_select_user_must_return_single_user(
    memory_model: Model, username: str, password: str
) -> None:
    user = memory_model.select_user(username=username, password=password)

    assert isinstance(user, User)
    assert user is not None


@mark.parametrize('idtodo', [index for index in range(1, len(TODOS) + 1)])
def test_select_todo_must_return_single_todo(
    memory_model: Model, idtodo: int
) -> None:
    todo = memory_model.select_todo(idtodo=idtodo)

    assert todo is not None


@mark.parametrize('iduser, username, email, password', UPDATED_USERS)
def test_update_user_must_persist_data(
    memory_model: Model,
    iduser: int,
    username: str,
    email: typing.Optional[str],
    password: str,
) -> None:
    pre_update_user = memory_model.select_user(iduser=iduser)
    pre_update_user.username = username
    pre_update_user.email = email
    pre_update_user.password = password

    memory_model.update_user(pre_update_user)
    pos_update_user = memory_model.select_user(iduser=iduser)

    assert pos_update_user.username == username
    assert pos_update_user.password == password
    assert pos_update_user.email == email


@mark.parametrize('idtodo, description, is_completed', UPDATED_TODOS)
def test_update_todo_must_persist_data(
    memory_model: Model, idtodo: int, description: str, is_completed: bool
) -> None:
    pre_update_todo = memory_model.select_todo(idtodo=idtodo)
    pre_update_todo.description = description
    pre_update_todo.is_completed = is_completed

    memory_model.update_todo(pre_update_todo)
    pos_update_todo = memory_model.select_todo(idtodo=idtodo)

    assert pos_update_todo.description == description
    assert pos_update_todo.is_completed == is_completed


@mark.parametrize('iduser', (user[0] for user in UPDATED_USERS))
def test_delete_user_must_persist_data(
    memory_model: Model, iduser: int
) -> None:
    user = memory_model.select_user(iduser=iduser)
    memory_model.delete_user(user)

    assert memory_model.select_user(iduser=iduser) is None


@mark.parametrize('idtodo', (todo[0] for todo in UPDATED_TODOS))
def test_delete_todo_must_persist_data(
    memory_model: Model, idtodo: int
) -> None:
    todo = memory_model.select_todo(idtodo=idtodo)
    memory_model.delete_todo(todo)

    assert memory_model.select_todo(idtodo=idtodo) is None
