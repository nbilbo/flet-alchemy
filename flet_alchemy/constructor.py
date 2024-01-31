import flet as ft

from flet_alchemy.application import Application
from flet_alchemy.application import AuthView
from flet_alchemy.application import GeneralView
from flet_alchemy.application import HomeView
from flet_alchemy.application import LoginUserView
from flet_alchemy.application import RegisterUserView
from flet_alchemy.application import TodoPreview
from flet_alchemy.controller import DeleteTodoController 
from flet_alchemy.controller import LoginUserController
from flet_alchemy.controller import RegisterTodoController
from flet_alchemy.controller import RegisterUserController
from flet_alchemy.controller import QueryCompletedTodoController
from flet_alchemy.controller import QueryIncompletedTodoController
from flet_alchemy.controller import QueryUserController
from flet_alchemy.controller import ToggleTodoController
from flet_alchemy.model import get_current_id_user
from flet_alchemy.model import set_current_id_user 
from flet_alchemy.settings import Settings


class Constructor:
    def __init__(self, page: ft.Page) -> None:
        self.application = Application(page)
        self.create_default_user()

        self.bind_auth_view(self.application.login_user_view)
        self.bind_auth_view(self.application.register_user_view)
        self.bind_login_user_view(self.application.login_user_view)
        self.bind_register_user_view(self.application.register_user_view)

        self.bind_general_view(self.application.home_view)
        self.bind_home_view(self.application.home_view)


    def bind_auth_view(self, view: AuthView) -> None:
        appbar_toggle_theme_button = view.appbar.toggle_theme_button
        appbar_toggle_theme_button.on_click = self.handle_toggle_theme_mode

        appbar_login_buttton = view.appbar.login_button
        appbar_login_buttton.on_click = self.handle_go_to_login_user_view

        appbar_register_buttton = view.appbar.register_button
        appbar_register_buttton.on_click = self.handle_go_to_register_user_view

    def bind_login_user_view(self, view: LoginUserView) -> None:
        login_button = view.login_button
        login_button.on_click = self.handle_login_user

        dont_account_button = view.dont_account_button
        dont_account_button.on_click = self.handle_go_to_register_user_view

    def bind_register_user_view(self, view: RegisterUserView) -> None:
        register_button = view.register_button
        register_button.on_click = self.handle_register_user

        already_account_button = view.already_account_button
        already_account_button.on_click = self.handle_go_to_login_user_view

    def bind_general_view(self, view: GeneralView) -> None:
        appbar_toggle_theme_button = view.appbar.toggle_theme_button
        appbar_toggle_theme_button.on_click = self.handle_toggle_theme_mode

        appbar_logout_button = view.appbar.logout_button
        appbar_logout_button.on_click = self.handle_logout

    def bind_home_view(self, view: HomeView) -> None:
        register_button = view.register_button
        register_button.on_click = self.handle_register_todo

        description_field = view.description_field
        description_field.on_submit = self.handle_register_todo

    def bind_completed_todos(self) -> None:
        todos = self.application.get_completed_todos()
        for todo in todos:
            toggle_completed_button = todo.toggle_completed_button
            toggle_completed_button.on_click = lambda _event, todo=todo: self.handle_toggle_todo(todo)

            delete_button = todo.delete_button
            delete_button.on_click = lambda _event, todo=todo: self.handle_delete_todo(todo)

    def bind_incompleted_todos(self) -> None:
        todos = self.application.get_incompleted_todos()
        for todo in todos:
            toggle_completed_button = todo.toggle_completed_button
            toggle_completed_button.on_click = lambda _event, todo=todo: self.handle_toggle_todo(todo)

            delete_button = todo.delete_button
            delete_button.on_click = lambda _event, todo=todo: self.handle_delete_todo(todo)

    def bind_todos(self) -> None:
        todos = self.application.get_todos()
        for todo in todos:
            toggle_completed_button = todo.toggle_completed_button
            toggle_completed_button.on_click = lambda _event, todo=todo: self.handle_toggle_todo(todo)

    def handle_go_to_login_user_view(self, _event: ft.ControlEvent) -> None:
        self.application.go_to_login_user_view()

    def handle_go_to_register_user_view(self, _event: ft.ControlEvent) -> None:
        self.application.go_to_register_user_view()

    def handle_toggle_theme_mode(self, _event: ft.ControlEvent) -> None:
        self.application.toggle_theme_mode()

    def handle_register_user(self, _event: ft.ControlEvent) -> None:
        self.application.clear_register_user_error_text()
        self.application.close_banner()

        register_informations = self.application.get_register_user_informations()
        controller = RegisterUserController()
        response = controller.register(register_informations)
        # print(f'[LOG Constructor.handle_register_user] {response}')

        if response.get('success'):
            set_current_id_user(response['message']['id'])
            self.application.go_to_home_view()
            self.application.focus_incompleted_todo_tab()
            self.application.clear_auth_views()
            self.application.clear_general_views()
            self.application.show_info_snack_bar('Welcome')
            self.refresh_todos()

        else:
            error = response.get('error')
            field = response.get('field')

            if field is not None:
                self.application.set_register_user_error_text(error, field)

            else:
                self.application.show_warning_banner(error)

    def handle_login_user(self, _event: ft.ControlEvent) -> None:
        self.application.clear_login_user_error_text()
        self.application.close_banner()

        login_informations = self.application.get_login_user_informations()
        controller = LoginUserController()
        response = controller.login(login_informations)
        # print(f'[LOG Constructor.handle_login_user] {response}')

        if response.get('success'):
            set_current_id_user(response['message']['id'])
            self.application.go_to_home_view()
            self.application.focus_incompleted_todo_tab()
            self.application.clear_auth_views()
            self.application.clear_general_views()
            self.application.show_info_snack_bar('Welcome')
            self.refresh_todos()

        else:
            error = response.get('error')
            field = response.get('field')

            if field is not None:
                self.application.set_login_user_error_text(error, field)

            else:
                self.application.show_warning_banner(error)

    def handle_logout(self, _event: ft.ControlEvent) -> None:
        query_informations = {'id_user': get_current_id_user()}
        controller = QueryUserController()
        response = controller.query(query_informations)

        if response.get('success'):
            username = response['message']['username']
            password = response['message']['password']
            self.application.set_login_user_values(username=username, password=password)
            set_current_id_user(None)

        self.application.go_to_login_user_view()
        self.application.set_completed_todos([])
        self.application.set_incompleted_todos([])

    def handle_register_todo(self, _event: ft.ControlEvent) -> None:
        self.application.clear_register_todo_error_text()
        self.application.close_banner()

        register_informations = self.application.get_register_todo_informations()
        register_informations.update({'id_user': get_current_id_user()})

        controller = RegisterTodoController()
        response = controller.register(register_informations)
        # print(f'[LOG Constructor.handle_register_todo] {response}')

        if response.get('success'):
            self.application.clear_general_views()
            self.application.focus_incompleted_todo_tab()
            self.refresh_todos()

        else:
            error = response.get('error')
            field = response.get('field')

            if field is not None:
                self.application.set_register_todo_error_text(error, 'description')
            
            else:
                self.application.show_warning_banner(error)

    def handle_toggle_todo(self, todo: TodoPreview) -> None:
        todo_informations = {'id_todo': todo.id_todo}
        controller = ToggleTodoController()
        response = controller.toggle(todo_informations)
        # print(f'[LOG Constructor.handle_toggle_todo] {response}')

        if response.get('success'):
            self.refresh_todos()
            self.application.clear_general_views()
            completed = response['message']['completed']

            if completed: self.application.focus_completed_todo_tab()
            else: self.application.focus_incompleted_todo_tab()

        else:
            error = response.get('error')
            self.application.show_warning_banner(error)

    def handle_delete_todo(self, todo: TodoPreview) -> None:
        todo_informations = {'id_todo': todo.id_todo}
        controller = DeleteTodoController()
        response = controller.delete(todo_informations)

        if response.get('success'):
            self.refresh_todos()
            self.application.clear_general_views()

        else:
            error =response.get('error')
            self.application.show_warning_banner(error)

    def refresh_completed_todos(self) -> None:
        query_informations = {'id_user': get_current_id_user()}
        controller = QueryCompletedTodoController()
        response = controller.query(query_informations)
        # print(f'[LOG Constructor.refresh_completed_todos] {response}')

        if response.get('success'):
            self.application.set_completed_todos(response.get('message'))
            self.bind_completed_todos()

        else:
            error = response.get('error')
            self.application.show_warning_banner(error)

    def refresh_incompleted_todos(self) -> None:
        query_informations = {'id_user': get_current_id_user()}
        controller = QueryIncompletedTodoController()
        response = controller.query(query_informations)
        # print(f'[LOG Constructor.refresh_incompleted_todos] {response}')

        if response.get('success'):
            self.application.set_incompleted_todos(response.get('message'))
            self.bind_incompleted_todos()

        else:
            error = response.get('error')
            self.application.show_warning_banner(error)

    def refresh_todos(self) -> None:
        self.refresh_completed_todos()
        self.refresh_incompleted_todos()

    def create_default_user(self) -> None:
        settings = Settings()
        username = settings.DEFAULT_USERNAME
        password = settings.DEFAULT_PASSWORD

        login_controller = LoginUserController()
        login_response = login_controller.login({'username': username, 'password': password})
        if login_response.get('success'):
            self.application.set_login_user_values(username=username, password=password)

        else:
            register_controller = RegisterUserController()
            register_response = register_controller.register({'username': username, 'password': password})
            if register_response.get('success'):
                self.application.set_login_user_values(username=username, password=password)
