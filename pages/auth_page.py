import time

from settings import valid_email, sql_injection, random_int
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from .locators import BaseLocators, AuthPageLocators, ChangePassPageLocators, RegPageLocators, \
    UserAgreementPageLocators, RejectedRequestPageLocators


class AuthPage(BasePage):
    # rs01 метод проверки перехода на форму авторизации
    def the_authorization_form_is_open(self):
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # rs02 метод проверки расположения меню выбора типа аутентификации
    def location_of_the_tab_menu(self):
        assert self.is_element_present(AuthPageLocators.AUTH_TAB_MENU), "element not found"

    # rs03 метод проверки типа аутентификации по умолчанию
    def default_authentication_type(self):
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # rs04 метод проверки расположения логотипа и слогана
    def location_of_the_logo_and_slogan(self):
        assert self.is_element_present(AuthPageLocators.AUTH_LOGO), "element not found"
        assert self.is_element_present(AuthPageLocators.AUTH_SLOGAN), "element not found"

    # rs05 метод проверки автоматического изменения типа аутентификации
    def automatic_change_of_authentication_type(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_EMAIL), "element not found"

    # rs06 метод проверки ссылки на форму восстановления пароля
    def link_to_the_password_recovery_form(self):
        self.find_element(AuthPageLocators.AUTH_FORGOT_PASSWORD_LINK).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_HEADING), "element not found"

    # rs07 метод проверки ссылки на форму регистрации
    def link_to_the_registration_form(self):
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()
        assert self.is_element_present(RegPageLocators.REG_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               in self.browser.current_url, "url do not match"

    # rs08 метод проверки ссылки под кнопкой "Войти" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthPageLocators.AUTH_USER_AGREEMENT_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # rs09 метод проверки ссылки на страницу авторизации с помощью соцсети "Одноклассники"
    def link_to_social_od(self):
        self.find_element(AuthPageLocators.AUTH_SOCIAL_OD_LINK).click()
        assert "https://connect.ok.ru/" in self.browser.current_url, "url do not match"

    # rs10 метод проверки авторизации с по связке Email+Password
    def authorization_email_password(self):
        self.find_element(AuthPageLocators.AUTH_TAB_EMAIL).click()
        self.find_element(AuthPageLocators.AUTH_USER_EMAIL_INPUT).click()
        self.find_element(AuthPageLocators.AUTH_USER_EMAIL_INPUT).send_keys("vip.sibgatov87@mail.ru")
        self.find_element(AuthPageLocators.AUTH_USER_PASSWORD_INPUT).click()
        self.find_element(AuthPageLocators.AUTH_USER_PASSWORD_INPUT).send_keys("87_Skills_87")
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c/page" in self.browser.current_url, \
            "url do not match"

    # rs11 метод проверки авторизации по связке phone+password
    def authorization_phone_password(self):
        self.find_element(AuthPageLocators.AUTH_USER_PHONE_INPUT).click()
        self.find_element(AuthPageLocators.AUTH_USER_PHONE_INPUT).send_keys("+7 902 817-01-17")
        self.find_element(AuthPageLocators.AUTH_USER_PASSWORD_INPUT).send_keys("87_Skills_87")
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c/page?state" in self.browser.current_url, \
            "url do not match"

    # rs12 метод проверки авторизации по связке login+password
    def authorization_logi_password(self):
        self.find_element(AuthPageLocators.AUTH_USER_LOGIN_INPUT).click()
        self.find_element(AuthPageLocators.AUTH_USER_LOGIN_INPUT).send_keys("21qwerty21")
        self.find_element(AuthPageLocators.AUTH_USER_PASSWORD_INPUT).send_keys("87_Skills_87")
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c/page?state" in self.browser.current_url, \
            "url do not match"

    # rs13 метод проверки авторизации по связке personal account+password
    def authorization_personal_password(self):
        self.find_element(AuthPageLocators.AUTH_USER_PERSONAL_INPUT).click()
        self.find_element(AuthPageLocators.AUTH_USER_PERSONAL_INPUT).send_keys("345691238578")
        self.find_element(AuthPageLocators.AUTH_USER_PASSWORD_INPUT).send_keys("87_Skills_87")
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c/page?state" in self.browser.current_url, \
            "url do not match"
