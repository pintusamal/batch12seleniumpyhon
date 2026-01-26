from selenium.webdriver.common.by import By

from Pages.basic_action import BasicActions


class LoginPage(BasicActions):
    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    submit_btn = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self):
        self.type_word(self.username, "Admin")

    def enter_password(self):
        self.type_word(self.password, "admin123")

    def click_on_submit(self):
        self.click_me(self.submit_btn )
        self.double_method()