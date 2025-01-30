from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from localizadores.Urban_Routes_Locators import UrbanRoutesLocators
from verification_code import retrieve_phone_code
import time


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
     field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.FROM_FIELD))
     field.clear()  # <-- Asegura que el campo esté vacío antes de escribir
     field.send_keys(from_address)

    def set_to(self, to_address):
     field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.TO_FIELD))
     field.clear()  # <-- Asegura que el campo esté vacío antes de escribir
     field.send_keys(to_address)

    def get_from(self):
        field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.FROM_FIELD))
        return field.get_attribute("value")

    def get_to(self):
        field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.TO_FIELD))
        return field.get_attribute("value")

    def request_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF)).click()

    def enter_phone_number(self, phone_number):
        """Hace clic en el campo de teléfono y escribe el número."""
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(UrbanRoutesLocators.PHONE_FIELD_LABEL)).click()
        phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.PHONE_INPUT))
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def click_next(self):
        """Hace clic en el botón 'Siguiente' después de ingresar el número de teléfono."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.NEXT_BUTTON)).click()
    def enter_verification_code(self):
        """Obtiene el código de verificación y lo ingresa en el campo correspondiente."""
        time.sleep(5)  # Espera para asegurarse de que el código haya llegado
        code = retrieve_phone_code(self.driver)
        if not code:raise Exception("No se pudo obtener el código de verificación.")

        code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.CODE_INPUT))
        code_input.clear()
        code_input.send_keys(code)

    def confirm_code(self):
        """Hace clic en el botón 'Confirmar' después de ingresar el código de verificación."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.CONFIRM_BUTTON)).click()

    def confirm_phone_number(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.CONFIRM_BUTTON)).click()

    def verification_code(self):
        code = retrieve_phone_code(self.driver)  # Obtiene el código de verificación
        if not code:raise Exception("No se pudo obtener el código de verificación.")
        code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.CODE_INPUT))
        code_input.send_keys(code)

    def open_payment_method(self):
        """Hace clic en 'Método de pago'."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.PAYMENT_METHOD)).click()

    def add_card(self):
        """Hace clic en 'Agregar tarjeta'."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_BUTTON)).click()

    def enter_card_details(self, card_number, card_cvv):
        """Rellena los datos de la tarjeta y simula un cambio de enfoque en el campo CVV."""
        # Ingresar el número de la tarjeta
        card_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.CARD_NUMBER_INPUT))
        card_input.clear()
        card_input.send_keys(card_number + Keys.TAB + card_cvv)

        cvv_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.CARD_CVV_INPUT))

        # Simular pérdida de enfoque con TAB
        # cvv_input.send_keys(Keys.TAB)
        time.sleep(5)# Esperar un momento para que el botón "Agregar" se active

    def submit_card(self):
        """Hace clic en el botón 'Agregar'."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_SUBMIT)).click()

    def close_card_modal(self):
        """Cierra el modal después de agregar la tarjeta."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.CLOSE_MODAL)).click()