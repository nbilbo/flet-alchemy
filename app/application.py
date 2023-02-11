# python.
import typing

# 3rd.
import flet as ft

# local.
from app.components.banners.dangerous_banner import DangerousBanner
from app.components.banners.success_banner import SuccessBanner
from app.components.banners.warning_banner import WarningBanner
from app.components.dialogs.detail_dialog import DetailDialog
from app.components.dialogs.success_dialog import SuccessDialog
from app.components.items.completed_item import CompletedItem
from app.components.items.incompleted_item import IncompletedItem
from app.components.snacks.success_snack import SuccessSnack
from app.controller.controller import Controller
from app.model.model import Todo
from app.views.home_view import HomeView
from app.views.login_view import LoginView
from app.views.logout_view import LogoutView
from app.views.register_view import RegisterView


class Application(object):
    def __init__(self, page: ft.Page) -> None:
        """Create the graphical user interface and start the Controller layer."""

        # first, the widgets.
        self.page = page
        self.login_view = LoginView()
        self.logout_view = LogoutView()
        self.home_view = HomeView()
        self.register_view = RegisterView()

        # anothers configurations.
        self.page.title = 'Todo Application'
        self.page.theme_mode = 'light'
        self.page.fonts = {
            'Cartis': 'fonts/cartis_beautyful/Cartis Beautyful serif.ttf',
            'Roboto-Medium': 'fonts/roboto/Roboto-Medium.ttf',
        }

        # initial state.
        self.show_login_view()

        # now, with all widgets created, we can start the controller layer.
        self.controller = Controller(self)

    def show_login_view(self) -> None:
        """Show login view."""
        self.page.views.clear()
        self.page.views.append(self.login_view)
        self.page.update()

    def show_logout_view(self) -> None:
        """Show logout view."""
        self.page.views.clear()
        self.page.views.append(self.logout_view)
        self.page.update()

    def show_home_view(self) -> None:
        """Show home view."""
        self.page.views.clear()
        self.page.views.append(self.home_view)
        self.page.update()

    def show_register_view(self) -> None:
        """Show register view."""
        self.page.views.clear()
        self.page.views.append(self.register_view)
        self.page.update()

    def display_success_banner_message(self, message: str) -> None:
        """Display a success message in a banner."""
        self.page.banner = SuccessBanner(self.page, message)
        self.page.banner.open = True
        self.page.update()

    def display_warning_banner_message(self, message: str) -> None:
        """Display a warning message in a banner."""
        self.page.banner = WarningBanner(self.page, message)
        self.page.banner.open = True
        self.page.update()

    def display_dangerous_banner_message(self, message: str) -> None:
        """Display a dangerous message in a banner."""
        self.page.banner = DangerousBanner(self.page, message)
        self.page.banner.open = True
        self.page.update()

    def display_success_snack_message(self, message: str) -> None:
        """Display a success message in a snackbar."""
        self.page.snack_bar = SuccessSnack(message)
        self.page.snack_bar.open = True
        self.page.update()

    def display_detail_dialog_message(self, title: str, message: str) -> None:
        """Display a detail message in a dialog."""
        self.page.dialog = DetailDialog(title, message)
        self.page.dialog.open = True
        self.page.update()

    def display_success_dialog_message(self, title: str, message: str) -> None:
        """Display a success message in a dialog."""
        self.page.dialog = SuccessDialog(title, message)
        self.page.dialog.open = True
        self.page.update()

    def hide_banner(self) -> None:
        """Hide the banner."""
        if self.page.banner is not None:
            self.page.banner.open = False
            self.page.update()

    def refresh_completed(self, todos: typing.List[Todo]) -> None:
        """Refresh the completed todo list."""
        listview = self.home_view.completed_tab.listview
        listview.controls.clear()
        for todo in todos:
            item = CompletedItem(
                identification=todo.idtodo, description=todo.description
            )
            listview.controls.append(item)
        self.page.update()

    def refresh_incompleted(self, todos: typing.List[Todo]) -> None:
        """Refresh the incompleted todo list."""
        listview = self.home_view.incompleted_tab.listview
        listview.controls.clear()
        for todo in todos:
            item = IncompletedItem(
                identification=todo.idtodo, description=todo.description
            )
            listview.controls.append(item)
        self.page.update()

    def clear_register_form(self) -> None:
        """Clear all fields in register form."""
        form = self.register_view.form
        form.username_field.value = ''
        form.password_field.value = ''
        form.email_field.value = ''
        self.page.update()

    def clear_login_form(self) -> None:
        """Clear all fields in login form."""
        form = self.login_view.form
        form.username_field.value = ''
        form.password_field.value = ''
        self.page.update()

    def clear_todo_form(self) -> None:
        """Clear all fields in todo form."""
        form = self.home_view.form
        form.description_field.value = ''
        self.page.update()

    def focus_todo_form(self) -> None:
        """Focus the todo form."""
        self.home_view.form.description_field.focus()
        self.page.update()

    def focus_incompleted_tab(self) -> None:
        """Focus the incompleted tab."""
        tabs = self.home_view.tabs
        tab = self.home_view.incompleted_tab
        tabs.selected_index = tabs.tabs.index(tab)
        self.page.update()

    def focus_completed_tab(self) -> None:
        """Focus the completed tab."""
        tabs = self.home_view.tabs
        tab = self.home_view.completed_tab
        tabs.selected_index = tabs.tabs.index(tab)
        self.page.update()

    def get_login_form(self) -> typing.Dict[str, typing.Optional[str]]:
        """Get the values for each field in login form."""
        form = self.login_view.form
        username = form.username_field.value.strip()
        password = form.password_field.value.strip()

        return {
            'username': username if len(username) else None,
            'password': password if len(password) else None,
        }

    def get_register_form(self) -> typing.Dict[str, typing.Optional[str]]:
        """Get the values for each field in register form."""
        form = self.register_view.form
        username = form.username_field.value.strip()
        password = form.password_field.value.strip()
        email = form.email_field.value.strip()

        return {
            'username': username if len(username) else None,
            'password': password if len(password) else None,
            'email': email if len(email) else None,
        }

    def get_todo_form(self) -> typing.Dict[str, typing.Optional[str]]:
        """Get the values for each field in todo form."""
        form = self.home_view.form
        description = form.description_field.value.strip()

        return {
            'description': description if len(description) else None,
            'is_completed': False,
        }

    def get_incompleted_items(self) -> typing.List[IncompletedItem]:
        """Get each item in incompleted list."""
        listview = self.home_view.incompleted_tab.listview
        return listview.controls

    def get_completed_items(self) -> typing.List[CompletedItem]:
        """Get each item in completed list."""
        listview = self.home_view.completed_tab.listview
        return listview.controls

    @property
    def login_button(self) -> ft.OutlinedButton:
        return self.login_view.form.login_button

    @property
    def register_button(self) -> ft.OutlinedButton:
        return self.register_view.form.register_button

    @property
    def no_account_button(self) -> ft.TextButton:
        return self.login_view.form.register_button

    @property
    def already_account_button(self) -> ft.TextButton:
        return self.register_view.form.login_button

    @property
    def exit_button(self) -> ft.IconButton:
        return self.home_view.appbar.exit_button

    @property
    def about_button(self) -> ft.IconButton:
        return self.home_view.appbar.about_button

    @property
    def add_todo_button(self) -> ft.IconButton:
        return self.home_view.form.add_button
