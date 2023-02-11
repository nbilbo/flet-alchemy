# python.
import typing

# local.
from app import constants
from app.components.items.completed_item import CompletedItem
from app.components.items.incompleted_item import IncompletedItem
from app.model.exceptions import EmailAlreadyRegistered
from app.model.exceptions import MissingField
from app.model.exceptions import UsernameAlreadyRegistered
from app.model.model import Model
from app.model.model import User
from app.model.model import Todo

if typing.TYPE_CHECKING:
    from app.application import Application


class Controller(object):
    def __init__(self, application: 'Application') -> None:
        """Manage application widgets and start the Model layer."""
        self.application = application
        self.model = Model(constants.DB_NAME)
        self.user = None

        self.application.login_button.on_click = (
            lambda event: self.login_action()
        )
        self.application.register_button.on_click = (
            lambda event: self.register_action()
        )
        self.application.no_account_button.on_click = (
            lambda event: self.no_account_action()
        )
        self.application.already_account_button.on_click = (
            lambda event: self.already_account_action()
        )
        self.application.exit_button.on_click = (
            lambda event: self.exit_action()
        )
        self.application.about_button.on_click = (
            lambda event: self.about_action()
        )
        self.application.add_todo_button.on_click = (
            lambda event: self.add_todo_action()
        )

    def login_action(self) -> None:
        """When login button has clicked."""
        self.application.hide_banner()
        form = self.application.get_login_form()
        username = form.get('username')
        password = form.get('password')
        user = self.model.select_user(username=username, password=password)

        if user is not None:
            self.user = user
            self.refresh_application()
            self.application.clear_login_form()
            self.application.clear_register_form()
            self.application.show_home_view()
            self.application.focus_incompleted_tab()
            self.application.display_success_snack_message(
                f'Welcome {self.user.username}'
            )
        else:
            self.application.display_warning_banner_message(
                'Username or password incorrectly'
            )

    def register_action(self) -> None:
        """When register button has clicked."""
        try:
            self.application.hide_banner()
            form = self.application.get_register_form()
            username = form.get('username')
            email = form.get('email')
            password = form.get('password')

            user = User(username=username, email=email, password=password)
            self.model.insert_user(user)
            self.user = user

            self.refresh_application()
            self.application.clear_login_form()
            self.application.clear_register_form()
            self.application.show_home_view()
            self.application.focus_incompleted_tab()
            self.application.display_success_snack_message(
                'Account successfully created.'
            )

        except MissingField as error:
            self.application.display_warning_banner_message(
                'Please, fill all required fields.'
            )

        except UsernameAlreadyRegistered as error:
            self.application.display_warning_banner_message(
                'Sorry, this username already registered.'
            )

        except EmailAlreadyRegistered:
            self.application.display_warning_banner_message(
                'Sorry, this email already registered.'
            )

        except Exception as error:
            print(error)
            self.application.display_dangerous_banner_message(str(error))

    def no_account_action(self) -> None:
        """When "dont have account" button has clicked."""
        self.application.hide_banner()
        self.application.show_register_view()

    def already_account_action(self) -> None:
        """When "already have account" button has clicked."""
        self.application.hide_banner()
        self.application.show_login_view()

    def exit_action(self) -> None:
        """When exit button has clicked."""
        self.user = None
        self.application.show_login_view()
        self.application.hide_banner()

    def about_action(self) -> None:
        """When about button has clicked."""
        self.application.display_detail_dialog_message(
            'About', 'Todo Application V.1.0'
        )

    def add_todo_action(self) -> None:
        """When add button has clicked."""
        try:
            self.application.hide_banner()
            form = self.application.get_todo_form()
            description = form.get('description')
            is_completed = form.get('is_completed')
            todo = Todo(
                description=description,
                is_completed=is_completed,
                user=self.user,
            )
            self.model.insert_todo(todo)

            self.refresh_application()
            self.application.clear_todo_form()
            self.application.display_success_snack_message(
                'ToDo successfully registered.'
            )
            self.application.focus_todo_form()
            self.application.focus_incompleted_tab()

        except MissingField as error:
            self.application.display_warning_banner_message(
                'Please, fill all required fields.'
            )

        except Exception as error:
            print(error)
            self.application.display_dangerous_banner_message(str(error))

    def delete_button_action(self, item) -> None:
        """When delete button has clicked."""
        try:
            todo = self.model.select_todo(idtodo=item.identification)
            self.model.delete_todo(todo)
            self.refresh_application()
            self.application.display_success_snack_message(
                'Successfully deleted.'
            )

        except Exception as error:
            print(error)
            self.application.display_dangerous_banner_message(str(error))

    def complete_button_action(self, item: IncompletedItem) -> None:
        """When complete button has clicked."""
        try:
            todo = self.model.select_todo(idtodo=item.identification)
            todo.is_completed = True
            self.model.update_todo(todo)
            self.refresh_application()
            self.application.focus_completed_tab()
            self.application.display_success_snack_message(
                'Successfully Updated.'
            )

        except Exception as error:
            print(error)
            self.application.display_dangerous_banner_message(str(error))

    def incomplete_button_action(self, item: CompletedItem) -> None:
        """When incomplete button has clicked."""
        try:
            todo = self.model.select_todo(idtodo=item.identification)
            todo.is_completed = False
            self.model.update_todo(todo)
            self.refresh_application()
            self.application.focus_incompleted_tab()
            self.application.display_success_snack_message(
                'Successfully Updated.'
            )

        except Exception as error:
            print(error)
            self.application.display_dangerous_banner_message(str(error))

    def refresh_application(self) -> None:
        """Refresh todo items."""
        completed = self.model.select_todos(user=self.user, is_completed=True)
        incompleted = self.model.select_todos(
            user=self.user, is_completed=False
        )
        self.application.refresh_incompleted(incompleted)
        self.application.refresh_completed(completed)
        self.bind_items()

    def bind_items(self) -> None:
        """Bind todo items."""
        for item in self.application.get_incompleted_items():
            item.delete_button.on_click = (
                lambda event, item=item: self.delete_button_action(item)
            )
            item.complete_button.on_click = (
                lambda event, item=item: self.complete_button_action(item)
            )

        for item in self.application.get_completed_items():
            item.delete_button.on_click = (
                lambda event, item=item: self.delete_button_action(item)
            )
            item.incomplete_button.on_click = (
                lambda event, item=item: self.incomplete_button_action(item)
            )
