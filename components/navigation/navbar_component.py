from playwright.sync_api import Page
import allure
from elements.text import Text
from components.base_component import BaseComponent


class NavBarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App Title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome text')
    @allure.step('Check visible navbar with username "{username}"')
    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
