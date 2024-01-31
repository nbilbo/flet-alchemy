from typing import Any
from typing import Dict
from typing import List

from flet_alchemy.exceptions import FieldException 
from flet_alchemy.model import Todo
from flet_alchemy.model import User
from flet_alchemy.model import get_session


class QueryUserController:
    def query(self, query_informations: Dict[Any, Any]) -> None:
        try:
            self.__valid_fields(query_informations)
            user = self.__find(query_informations)
            message = {'id': user.id, 'username': user.username, 'password': user.password}

        except FieldException as exc:
            return {'success': False, 'error': str(exc), 'field': exc.field}

        except Exception as exc:
            return {'success': False, 'error': str(exc)}

        else:
            return {'success': True, 'message': message}


    def __valid_fields(self, query_informations: Dict[Any, Any]) -> None:
        id_user = query_informations.get('id_user', None)
        username = query_informations.get('username', None)

        if id_user is not None and not isinstance(id_user, int):
            raise FieldException('id_user must be integer', 'id_user')

        if username is not None and not isinstance(username, str):
            raise FieldException('username must be string', 'username')

    def __find(self, query_informations: Dict[Any, Any]) -> User:
        id_user = query_informations.get('id_user', None)
        username = query_informations.get('username', None)
        session = get_session()
        select = session.query(User)

        if id_user is not None:
            select = select.filter(User.id == id_user)

        if username is not None:
            select = select.filter(User.username == username)

        user = select.first()
        if user is None: raise Exception('User not found')

        return user


class LoginUserController:
    def login(self, login_informations: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self.__valid_fields(login_informations)
            user = self.__auth(login_informations)
            message = {'id': user.id, 'username': user.username}

        except FieldException as exc:
            return {'success': False, 'error': str(exc), 'field': exc.field}

        except Exception as exc:
            return {'success': False, 'error': str(exc)}

        else:
            return {'success': True, 'message': message}

    def __valid_fields(self, login_informations: Dict[Any, Any]) -> None:
        username = login_informations.get('username', '')
        password = login_informations.get('password', '')

        if not len(username):
            raise FieldException('username cant be blank', 'username')

        if not len(password):
            raise FieldException('password cant be blank', 'password')

    def __auth(self, login_informations: Dict[Any, Any]) -> User:
        username = login_informations.get('username')
        password = login_informations.get('password')
        session = get_session()

        users = session.query(User).filter(User.username == username, User.password == password).all()
        if users: return users[0]

        raise FieldException('username or password invalid', 'username')


class RegisterUserController:
    def register(self, register_informations: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self.__valid_fields(register_informations)
            user = self.__create_user(register_informations)
            message = {'id': user.id, 'username': user.username}

        except FieldException as exc:
            return {'success': False, 'error': str(exc), 'field': exc.field}

        except Exception as exc:
            return {'success': False, 'error': str(exc)}

        else:
            return {'success': True, 'message': message}

    def __valid_fields(self, register_informations: Dict[Any, Any]) -> None:
        username = register_informations.get('username', '')
        password = register_informations.get('password', '')
        session = get_session()

        if not len(username):
            raise FieldException('username cant be blank', field='username')

        elif not len(password):
            raise FieldException('password cant be blank', field='password')

        elif session.query(User).filter(User.username == username).all():
            raise FieldException('username already registered', field='username')

    def __create_user(self, register_informations: Dict[Any, Any]) -> User:
        username = register_informations.get('username')
        password = register_informations.get('password')
        user = User(username=username, password=password)

        session = get_session()
        session.add(user)
        session.commit()
        session.refresh(user)

        return user


class RegisterTodoController:
    def register(self, register_informations: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self.__valid_fields(register_informations)
            todo = self.__create_todo(register_informations)

            message = {
                'id': todo.id, 
                'description': todo.description, 
                'completed': todo.completed,
                'id_user': todo.id_user
            }

        except FieldException as exc:
            return {'success': False, 'error': str(exc), 'field': exc.field}

        except Exception as exc:
            return {'success': False, 'error': str(exc)}

        else:
            return {'success': True, 'message': message}

    def __valid_fields(self, register_informations: Dict[Any, Any]) -> None:
        description = register_informations.get('description', None)
        completed = register_informations.get('completed', None)
        id_user = register_informations.get('id_user', None)

        if description is None:
            raise FieldException('description cant be None', 'description')

        elif completed is None:
            raise FieldException('completed cant be None', 'completed')

        elif id_user is None:
            raise FieldException('id_user cant be None', 'id_user')

        elif not isinstance(description, str):
            raise FieldException('description must be string', 'description')

        elif not isinstance(completed, bool):
            raise FieldException('completed must be boolean', 'completed')

        elif not isinstance(id_user, int):
            raise FieldException('id_user must be integer', 'id_user')

        elif not len(description):
            raise FieldException('description cant be blank', 'description')

    def __create_todo(self, register_informations: Dict[Any, Any]) -> Todo:
        description = register_informations.get('description', None)
        completed = register_informations.get('completed', None)
        id_user = register_informations.get('id_user', None)
        session = get_session()

        user = session.query(User).filter(User.id == id_user).first()
        if user is None: 
            raise Exception('User not found')
        
        todo = Todo(description=description, completed=completed, user=user)
        session.add(todo)
        session.commit()
        session.refresh(todo)

        return todo


class QueryCompletedTodoController:
    def query(self, query_informations: Dict[Any, Any]) -> List[Todo]:
        try:
            self.__valid_fields(query_informations)
            completed_todos = self.__find(query_informations)

        except Exception as exc:
            return {'success': False, 'error': str(exc)}
        
        else:
            return {'success': True, 'message': completed_todos}

    def __valid_fields(self, query_informations: Dict[Any, Any]) -> None:
        id_user = query_informations.get('id_user', None)

        if id_user is None:
            raise Exception('id_user cant be None')

        elif not isinstance(id_user, int):
            raise Exception('id_user must be integer')

    def __find(self, query_informations: Dict[Any, Any]) -> List[Todo]:
        id_user = query_informations.get('id_user')
        session = get_session()
        completed_todos = session.query(Todo).where(Todo.id_user == id_user, Todo.completed == True).all()

        return completed_todos


class QueryIncompletedTodoController:
    def query(self, query_informations: Dict[Any, Any]) -> List[Todo]:
        try:
            self.__valid_fields(query_informations)
            incompleted_todos = self.__find(query_informations)

        except Exception as exc:
            return {'success': False, 'error': str(exc)}
        
        else:
            return {'success': True, 'message': incompleted_todos}

    def __valid_fields(self, query_informations: Dict[Any, Any]) -> None:
        id_user = query_informations.get('id_user', None)

        if id_user is None:
            raise Exception('id_user cant be None')

        elif not isinstance(id_user, int):
            raise Exception('id_user must be integer')

    def __find(self, query_informations: Dict[Any, Any]) -> List[Todo]:
        id_user = query_informations.get('id_user')
        session = get_session()
        incompleted_todos = session.query(Todo).where(Todo.id_user == id_user, Todo.completed == False).all()

        return incompleted_todos


class ToggleTodoController:
    def toggle(self, todo_informations: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self.__valid_fields(todo_informations)
            todo = self.__toggle_todo(todo_informations)

            message = {
                'id': todo.id, 
                'description': todo.description, 
                'completed': todo.completed, 
                'id_user': todo.user.id
            }

        except Exception as exc:
            return {'success': False, 'error': str(exc)}

        else:
            return {'success': True, 'message': message}

    def __valid_fields(self, todo_informations: Dict[Any, Any]) -> None:
        id_todo = todo_informations.get('id_todo', None)

        if id_todo is None:
            raise Exception('id_todo cant be None')

        if not isinstance(id_todo, int):
            raise Exception('id_todo must be integer')

    def __toggle_todo(self, todo_informations: Dict[Any, Any]) -> Todo:
        id_todo = todo_informations.get('id_todo')
        session = get_session()
        todo = session.query(Todo).filter(Todo.id == id_todo).first()

        if todo is not None:
            todo.completed = not todo.completed
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo

        raise Exception('Todo not found')


class DeleteTodoController:
    def delete(self, todo_informations: Dict[Any, Any]) -> Dict[Any, Any]:
        try:
            self.__valid_fields(todo_informations)
            self.__delete_todo(todo_informations)

        except Exception as exc:
            return {'success': False, 'error': str(exc)}

        else:
            return {'success': True}

    def __valid_fields(self, todo_informations: Dict[Any, Any]) -> None:
        id_todo = todo_informations.get('id_todo', None)

        if id_todo is None:
            raise Exception('id_todo cant be None')

        if not isinstance(id_todo, int):
            raise Exception('id_todo must be integer')

    def __delete_todo(self, todo_informations: Dict[Any, Any]) -> None:
        id_todo = todo_informations.get('id_todo', None)
        session = get_session()
        todo = session.query(Todo).filter(Todo.id == id_todo).first()

        if todo is None: 
            raise Exception('Todo not found')

        session.delete(todo)
        session.commit()
