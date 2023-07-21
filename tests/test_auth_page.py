from pages.auth_page import AuthPage
from settings import url_base_page


class TestAuthPage():
    def test_rs01_the_authorization_form_is_open(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.the_authorization_form_is_open()

    def test_rs02_location_of_the_tab_menu(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_of_the_tab_menu()

    def test_rs03_default_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.default_authentication_type()

    def test_rs04_location_of_the_logo_and_slogan(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_of_the_logo_and_slogan()

    def test_rs05_automatic_change_of_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.automatic_change_of_authentication_type()

    def test_rs06_link_to_the_password_recovery_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_password_recovery_form()

    def test_rs07_link_to_the_registration_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_registration_form()

    def test_rs08_link_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_user_agreement_page()

    def test_rs09_link_to_social_od(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_social_od()

    def test_rs10_authorization_email_password(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_email_password()

    def test_rs11_authorization_phone_password(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_phone_password()

    def test_rs12_authorization_logi_password(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_logi_password()

    def test_rs13_authorization_personal_password(self,browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_personal_password()


