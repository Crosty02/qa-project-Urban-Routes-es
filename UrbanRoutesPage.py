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
        """Rellena los datos de la tarjeta asegurando que el CVV esté visible y habilitado."""

        print("Esperando que el modal de 'Agregar tarjeta' se cargue completamente...")
        time.sleep(2)  # Espera extra para evitar problemas de carga

        # **Paso 1: Ingresar el número de la tarjeta**
        print("Esperando el campo de número de tarjeta...")
        card_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UrbanRoutesLocators.CARD_NUMBER_INPUT)
        )
        print("Campo de número de tarjeta encontrado y habilitado.")
        card_input.clear()
        card_input.send_keys(card_number)
        print(f"Número de tarjeta ingresado: {card_number}")

        # **Paso 2: Intentar detectar el CVV**
        try:
            print("Esperando el campo CVV...")
            cvv_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(UrbanRoutesLocators.CARD_CVV_INPUT)
            )
        except:
            print(
                "⚠️ No se encontró el campo CVV automáticamente. Intentando hacer clic en un espacio vacío para activarlo.")
            empty_space = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))  # Clic en el fondo de la página
            )
            empty_space.click()
            time.sleep(2)  # Esperar que la página reaccione

            # Intentar encontrar el CVV nuevamente
            cvv_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(UrbanRoutesLocators.CARD_CVV_INPUT)
            )

        print("Campo CVV encontrado y habilitado.")

        # **Paso 3: Ingresar el CVV**
        cvv_input.clear()
        cvv_input.send_keys(card_cvv)
        print(f"CVV ingresado correctamente: {card_cvv}")

        # **Paso 4: Simular pérdida de enfoque**
        cvv_input.send_keys(Keys.TAB)
        time.sleep(1)
        print("Campo CVV completado y enfoque cambiado.")

    def submit_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_SUBMIT)).click()

    def close_card_modal(self):
     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.CLOSE_MODAL)).click()

    def enter_driver_message(self, message):
        # Hacer clic en el label para activar el campo
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.MESSAGE_LABEL)).click()

        # Escribir el mensaje en el campo de entrada
        message_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.MESSAGE_INPUT))
        message_input.clear()
        message_input.send_keys(message)

    def request_blanket_tissues(self):
        # Hacer clic en la etiqueta para seleccionar la opción
        blanket_label = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.BLANKET_TISSUE_LABEL))
        blanket_label.click()

        # Activar el interruptor (si no está activado)
        switch = self.wait.until(EC.presence_of_element_located(UrbanRoutesLocators.BLANKET_TISSUE_SWITCH))
        if not switch.is_selected():  # Verificar si ya está activado
         self.driver.execute_script("arguments[0].click();", switch)


    def request_two_ice_creams(self):
        plus_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ICE_CREAM_PLUS_BUTTON))

    # Hacer clic dos veces para pedir 2 helados
        plus_button.click()
        time.sleep(1)  # Pequeño delay en caso de animación
        plus_button.click()

    def reserve_taxi(self):
        reserve_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.RESERVE_TAXI_BUTTON))
        reserve_button.click()

