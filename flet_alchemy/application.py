from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import flet as ft

from flet_alchemy.model import Todo


class AuthAppBar(ft.AppBar):
    def __init__(self) -> None:
        super().__init__()
        self.toolbar_height = 75

        self.leading = ft.IconButton()
        self.leading.icon = ft.Icons.SCIENCE

        self.title = ft.Text()
        self.title.value = 'Flet Alchemy'

        self.toggle_theme_button = ft.IconButton()
        self.toggle_theme_button.icon = ft.Icons.DARK_MODE

        self.login_button = ft.TextButton()
        self.login_button.text = 'Login'
        self.login_button.icon = ft.Icons.LOGIN_OUTLINED

        self.register_button = ft.TextButton()
        self.register_button.text = 'Register'
        self.register_button.icon = ft.Icons.EDIT_OUTLINED

        self.actions.append(self.login_button)
        self.actions.append(self.register_button)
        self.actions.append(self.toggle_theme_button)


class GeneralAppBar(ft.AppBar):
    def __init__(self) -> None:
        super().__init__()
        self.toolbar_height = 75

        self.leading = ft.IconButton()
        self.leading.icon = ft.Icons.SCIENCE

        self.title = ft.Text()
        self.title.value = 'Flet Alchemy'

        self.username = ft.Text()
        self.username.theme_style = ft.TextThemeStyle.LABEL_LARGE
        self.username.value = ''

        self.about_button = ft.PopupMenuItem()
        self.about_button.icon = ft.Icons.INFO
        self.about_button.text = 'About'

        self.logout_button = ft.PopupMenuItem()
        self.logout_button.icon = ft.Icons.LOGOUT
        self.logout_button.text = 'Logout'

        self.toggle_theme_button = ft.PopupMenuItem()
        self.toggle_theme_button.icon = ft.Icons.DARK_MODE
        self.toggle_theme_button.text = 'Theme'

        self.pop_menu = ft.PopupMenuButton()
        self.pop_menu.items.append(self.toggle_theme_button)
        self.pop_menu.items.append(self.about_button)
        self.pop_menu.items.append(self.logout_button)

        self.actions.append(ft.Row([ft.Icon(ft.Icons.FACE), self.username]))
        self.actions.append(self.pop_menu)


class AboutDialog(ft.AlertDialog):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        title = ft.Text()
        title.value = 'Flet Alchemy'
        title.theme_style = ft.TextThemeStyle.TITLE_LARGE
        title.text_align = ft.TextAlign.CENTER
        title.expand = True

        close_button = ft.FloatingActionButton()
        close_button.icon = ft.Icons.CLOSE
        close_button.bgcolor = ft.Colors.RED
        close_button.tooltip = 'Close'
        close_button.on_click = lambda _event: page.close(self)

        messages = [
            'Flet-Alchemy is a program for registering user tasks.',
            'Each user has their own tasks that can be viewed, updated, and deleted.',
            'The program also includes an authentication screen, registration screen, and home screen.'
        ]
        
        content = ft.Column()
        content.controls.append(ft.Row([close_button], alignment=ft.MainAxisAlignment.END))
        content.controls.append(ft.Row([title]))
        content.scroll = ft.ScrollMode.AUTO

        for message in messages:
            text = ft.Text()
            text.value = message
            text.text_align = ft.TextAlign.CENTER
            text.theme_style = ft.TextThemeStyle.LABEL_LARGE
            text.theme_style = ft.TextThemeStyle.BODY_LARGE
            text.selectable = True
            text.expand = True
            content.controls.append(ft.Row([text]))

        self.content = content


class AuthView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.appbar = AuthAppBar()

        self.title = ft.Text()
        self.title.theme_style = ft.TextThemeStyle.DISPLAY_LARGE
        self.title.text_align = ft.TextAlign.CENTER

        self.content = ft.Column()
        self.content.controls.append(self.title)
        self.content.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.container = ft.Container(self.content)
        self.container.border = ft.border.all(5, ft.Colors.TRANSPARENT)
        self.container.width = 600
        self.controls.append(self.container)


class GeneralView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.appbar = GeneralAppBar()
        self.content = ft.Column()

        self.container = ft.Container(self.content)
        self.container.width = 600
        self.container.border = ft.border.all(5, ft.Colors.TRANSPARENT)
        self.container.expand = True
        self.controls.append(self.container)


class LoginUserView(AuthView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/auth/login'
        self.appbar.login_button.icon = ft.Icons.LOGIN
        self.title.value = 'Login'

        self.username_field = ft.TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = ft.TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.login_button = ft.OutlinedButton()
        self.login_button.text = 'Login'
        self.login_button.expand = True

        self.dont_account_button = ft.TextButton()
        self.dont_account_button.text = 'Don\'t have an account? click here'
        self.dont_account_button.expand = True

        self.content.controls.append(ft.Row([self.username_field]))
        self.content.controls.append(ft.Row([self.password_field]))
        self.content.controls.append(ft.Row([self.login_button]))
        self.content.controls.append(ft.Row([self.dont_account_button]))


class RegisterUserView(AuthView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/auth/register'
        self.appbar.register_button.icon = ft.Icons.EDIT
        self.title.value = 'Register'

        self.username_field = ft.TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = ft.TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.register_button = ft.OutlinedButton()
        self.register_button.text = 'Register'
        self.register_button.expand = True

        self.already_account_button = ft.TextButton()
        self.already_account_button.text = 'Already have an account? click here'
        self.already_account_button.expand = True

        self.content.controls.append(ft.Row([self.username_field]))
        self.content.controls.append(ft.Row([self.password_field]))
        self.content.controls.append(ft.Row([self.register_button]))
        self.content.controls.append(ft.Row([self.already_account_button]))


class HomeView(GeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/'

        self.description_field = ft.TextField()
        self.description_field.label = 'What need to be done?'
        self.description_field.expand = True

        self.register_button = ft.FloatingActionButton()
        self.register_button.icon = ft.Icons.ADD

        self.incompleted_tab = IncompletedTab()
        self.completed_tab = CompletedTab()

        self.tabs = ft.Tabs()
        self.tabs.tabs.append(self.incompleted_tab)
        self.tabs.tabs.append(self.completed_tab)
        self.tabs.animation_duration = 350
        self.tabs.expand = True

        self.content.controls.append(ft.Row([self.description_field, self.register_button]))
        self.content.controls.append(self.tabs)


class IncompletedTab(ft.Tab):
    def __init__(self) -> None:
        super().__init__()
        self.text = 'Incompleted'
        self.icon = ft.Icons.CHECK_BOX_OUTLINE_BLANK

        self.list_view = ft.ListView()
        self.list_view.spacing = 25
        self.content = self.list_view


class CompletedTab(ft.Tab):
    def __init__(self) -> None:
        super().__init__()
        self.text = 'Completed'
        self.icon = ft.Icons.CHECK_BOX_OUTLINED

        self.list_view = ft.ListView()
        self.list_view.spacing = 25
        self.content = self.list_view


class TodoPreview(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.id_todo: Optional[int] = None

        self.description = ft.Text()
        self.description.theme_style = ft.TextThemeStyle.BODY_LARGE
        self.description.text_align = ft.TextAlign.CENTER
        self.description.expand = True

        self.toggle_completed_button = ft.IconButton()
        self.toggle_completed_button.icon = ft.Icons.CHECK_BOX

        self.delete_button = ft.IconButton()
        self.delete_button.icon = ft.Icons.DELETE
        self.delete_button.icon_color = ft.Colors.RED
        
        self.content = ft.Column()
        self.content.controls.append(ft.Row([self.delete_button, self.description, self.toggle_completed_button]))
        self.container = ft.Container(self.content)

    def build(self) -> ft.Container:
        return self.container


class WarningBanner(ft.Banner):
    def __init__(self, page: ft.Page, message: str) -> None:
        super().__init__()
        self.message = ft.Text()
        self.message.value = message
        self.message.theme_style = ft.TextThemeStyle.BODY_LARGE
        self.message.selectable = True
        self.message.expand = True

        self.icon = ft.Icon()
        self.icon.name = ft.Icons.WARNING

        self.close_button = ft.TextButton()
        self.close_button.text = 'Close'
        self.close_button.icon = ft.Icons.CLOSE
        self.close_button.on_click = lambda _event: page.close(self)

        self.content = ft.Column()
        self.content.controls.append(ft.Row([self.icon, self.message]))
        self.actions.append(self.close_button)


class InfoSnackBar(ft.SnackBar):
    def __init__(self, message: str) -> None:
        super().__init__(content=ft.Row())
        self.bgcolor = ft.Colors.TRANSPARENT

        self.message = ft.Text()
        self.message.value = message
        self.message.theme_style = ft.TextThemeStyle.BODY_LARGE
        self.message.expand = True

        self.icon = ft.Icon()
        self.icon.name = ft.Icons.INFO

        self.content.controls.append(self.icon)
        self.content.controls.append(self.message)


class Application:
    def __init__(self, page: ft.Page) -> None:
        self.snackbar: Optional[ft.SnackBar] = None
        self.dialog: Optional[ft.AlertDialog] = None
        self.banner: Optional[ft.Banner] = None

        self.page = page
        self.page.on_route_change = self.__route_change
        self.page.window.width = self.page.window.height = 500
        self.page.title = 'Flet Alchemy'
        
        self.home_view = HomeView()
        self.general_views: List[GeneralView] = [self.home_view]

        self.login_user_view = LoginUserView()
        self.register_user_view = RegisterUserView()
        self.auth_views: List[AuthView] = [self.login_user_view, self.register_user_view]

        self.go_to_login_user_view()
        self.active_dark_theme_mode()

        # debug.
        # self.go_to_home_view()
        # self.active_light_theme_mode()
        # self.show_info_snack_bar('vsf')

    def go_to_login_user_view(self) -> None:
        self.page.go(self.login_user_view.route)

    def go_to_register_user_view(self) -> None:
        self.page.go(self.register_user_view.route)

    def go_to_home_view(self) -> None:
        self.page.go(self.home_view.route)

    def active_dark_theme_mode(self) -> None:
        for view in self.auth_views:
            view.appbar.toggle_theme_button.icon = ft.Icons.LIGHT_MODE

        for view in self.general_views:
            view.appbar.toggle_theme_button.icon = ft.Icons.LIGHT_MODE
            view.appbar.toggle_theme_button.text = 'Light'

        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()

    def active_light_theme_mode(self) -> None:
        for view in self.auth_views:
            view.appbar.toggle_theme_button.icon = ft.Icons.DARK_MODE

        for view in self.general_views:
            view.appbar.toggle_theme_button.icon = ft.Icons.DARK_MODE
            view.appbar.toggle_theme_button.text = 'Dark'

        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

    def toggle_theme_mode(self) -> None:
        match(self.page.theme_mode):
            case ft.ThemeMode.DARK:
                self.active_light_theme_mode()
            case ft.ThemeMode.LIGHT:
                self.active_dark_theme_mode()

    def show_warning_banner(self, message: str) -> None:
        self.banner = WarningBanner(self.page, message)
        self.page.open(self.banner)

    def show_info_snack_bar(self, message: str) -> None:
        self.snackbar = InfoSnackBar(message)
        self.page.open(self.snackbar)

    def show_about_dialog(self) -> None:
        self.dialog = AboutDialog(self.page)
        self.page.open(self.dialog)

    def close_banner(self) -> None:
        if self.banner is not None:
            self.page.close(self.banner)
            self.banner = None

    def clear_login_user_error_text(self) -> None:
        for field in self.__get_login_user_fields().values():
            field.error_text = ''
        self.page.update()

    def clear_register_user_error_text(self) -> None:
        for field in self.__get_register_user_fields().values():
            field.error_text = ''
        self.page.update()

    def clear_register_todo_error_text(self) -> None:
        for field in self.__get_register_todo_fields().values():
            field.error_text = ''
        self.page.update()

    def clear_login_user_fields(self) -> None:
        for field in self.__get_login_user_fields().values():
            field.value = ''
        self.page.update()

    def clear_register_user_fields(self) -> None:
        for field in self.__get_register_user_fields().values():
            field.value = ''
        self.page.update()

    def clear_register_todo_fields(self) -> None:
        for field in self.__get_register_todo_fields().values():
            field.value = ''
        self.page.update()

    def clear_auth_views(self) -> None:
        self.clear_login_user_fields()
        self.clear_register_user_fields()

        self.clear_login_user_error_text()
        self.clear_register_user_error_text()

    def clear_general_views(self) -> None:
        self.clear_register_todo_fields()
        self.clear_register_todo_error_text()

    def focus_completed_todo_tab(self) -> None:
        tabs = self.home_view.tabs.tabs
        completed_tab = self.home_view.completed_tab
        index = tabs.index(completed_tab)
        self.home_view.tabs.selected_index = index
        self.page.update()

    def focus_incompleted_todo_tab(self) -> None:
        tabs = self.home_view.tabs.tabs
        incompleted_tab = self.home_view.incompleted_tab
        index = tabs.index(incompleted_tab)
        self.home_view.tabs.selected_index = index
        self.page.update()

    def get_login_user_informations(self) -> Dict[str, str]:
        username = self.login_user_view.username_field.value
        password = self.login_user_view.password_field.value

        return {'username': username, 'password': password}

    def get_register_user_informations(self) -> Dict[str, str]:
        username = self.register_user_view.username_field.value
        password = self.register_user_view.password_field.value

        return {'username': username, 'password': password}

    def get_register_todo_informations(self) -> Dict[Any, Any]:
        description = self.home_view.description_field.value

        return {'description': description, 'completed': False}

    def get_completed_todos(self) ->List[TodoPreview]:
        return self.home_view.completed_tab.list_view.controls

    def get_incompleted_todos(self) ->List[TodoPreview]:
        return self.home_view.incompleted_tab.list_view.controls

    def get_todos(self) -> List[TodoPreview]:
        return self.get_completed_todos() + self.get_incompleted_todos()
    
    def set_appbar_username(self, username: str) -> None:
        for view in self.general_views:
            view.appbar.username.value = username
        self.page.update()

    def set_login_user_error_text(self, message: str, field: str) -> None:
        fields = self.__get_login_user_fields()
        if field in fields.keys():
            fields[field].error_text = message
            self.page.update()

    def set_register_user_error_text(self, message: str, field: str) -> None:
        fields = self.__get_register_user_fields()
        if field in fields.keys():
            fields[field].error_text = message
            self.page.update()

    def set_register_todo_error_text(self, message: str, field: str) -> None:
        fields = self.__get_register_todo_fields()
        if field in fields.keys():
            fields[field].error_text = message
            self.page.update()

    def set_completed_todos(self, todos: List[Todo]) -> None:
        list_view = self.home_view.completed_tab.list_view
        list_view.controls.clear()

        for todo in todos:
            preview = TodoPreview()
            preview.id_todo = todo.id
            preview.description.value = todo.description
            preview.toggle_completed_button.icon = ft.Icons.CHECK_BOX_OUTLINED
            preview.toggle_completed_button.icon_color = ft.Colors.AMBER
            list_view.controls.append(preview)

        self.page.update()

    def set_incompleted_todos(self, todos: List[Todo]) -> None:
        list_view = self.home_view.incompleted_tab.list_view
        list_view.controls.clear()

        for todo in todos:
            preview = TodoPreview()
            preview.id_todo = todo.id
            preview.description.value = todo.description
            preview.toggle_completed_button.icon = ft.Icons.CHECK_BOX_OUTLINE_BLANK
            preview.toggle_completed_button.icon_color = ft.Colors.GREEN
            list_view.controls.append(preview)

        self.page.update()

    def set_login_user_values(self, username: str, password: str) -> None:
        self.login_user_view.username_field.value = username
        self.login_user_view.password_field.value = password
        self.page.update()

    def __get_login_user_fields(self) -> Dict[str, ft.TextField]:
        username_field = self.login_user_view.username_field
        password_field = self.login_user_view.password_field

        return {'username': username_field, 'password': password_field}

    def __get_register_user_fields(self) -> Dict[str, ft.TextField]:
        username_field = self.register_user_view.username_field
        password_field = self.register_user_view.password_field

        return {'username': username_field, 'password': password_field}
    
    def __get_register_todo_fields(self) -> Dict[Any, Any]:
        description_field = self.home_view.description_field

        return {'description': description_field}

    def __route_change(self, _route: ft.RouteChangeEvent) -> None:
        template_route = ft.TemplateRoute(self.page.route)
        self.page.views.clear()

        if template_route.match(self.login_user_view.route):
            self.page.views.append(self.login_user_view)

        elif template_route.match(self.register_user_view.route):
            self.page.views.append(self.register_user_view)

        elif template_route.match(self.home_view.route):
            self.page.views.append(self.home_view)
        
        self.page.update()
