from .base_page import BasePage
from .locators import BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators


class RegPage(BasePage):
    # rs19 метод проверки расположения полей ввода, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        assert self.is_element_present(RegPageLocators.REG_FIRST_NAME_INPUT_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_REGISTER_BUTTON_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_USER_AGREEMENT_LINK_PAGE_RIGHT), "element not found"

    # rs20 метод проверки регистрации с валидными данными
    def registration_with_valid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element not found"

    # rs21 метод проверки валидации поля ввода email или мобильного телефона (ввод невалидных данных)
    def email_or_phone_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element not found"

    # rs22 метод проверки валидации поля ввода пароля (ввод невалидных данных)
    def password_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element not found"

    # rs23 метод проверки заполнения поля подтверждения пароля данными, отличными от введенных в поле ввода пароля
    def entering_data_in_the_password_confirmation_field(self, password1, password2):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password1)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password2)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_PASSWORD_DONT_MATCH), "element not found"

    # rs24 метод проверки регистрации с невалидными данными
    def registration_with_invalid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_not_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element found"
