from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from localizadores.Urban_Routes_Locators import UrbanRoutesLocators
from verification_code import retrieve_phone_code
import time


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

     # 1 Confirmación del establecimiento de la ruta

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

    # 2 Prueba que verifica que se selecciona la tarifa Comfort

    def request_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)).click()

    def select_comfort_tariff(self):
        comfort_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF))
        comfort_element.click()

    def is_comfort_selected(self):
        # Esperar a que el div de Comfort tenga la clase "active"
        selected_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.COMFORT_TARIFF))
        # Obtener la clase del elemento después del clic
        element_class = selected_element.get_attribute("class")
        print(f"Clase del elemento después del clic: {element_class}")
        return "active" in element_class  # Verifica si tiene la clase "active"

    # 3 Prueba que verifica que se agrega el número de teléfono y el código de confirmation

    def enter_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.PHONE_FIELD_LABEL)).click()
        phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.PHONE_INPUT))
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def click_next(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.NEXT_BUTTON)).click()

    def enter_verification_code(self):
        time.sleep(5)  # Espera para asegurarse de que el código haya llegado
        code = retrieve_phone_code(self.driver)
        if not code:raise Exception("No se pudo obtener el código de verificación.")

        code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.CODE_INPUT))
        code_input.clear()
        code_input.send_keys(code)

    def verification_code(self):
        code = retrieve_phone_code(self.driver)  # Obtiene el código de verificación
        if not code:raise Exception("No se pudo obtener el código de verificación.")
        code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.CODE_INPUT))
        code_input.send_keys(code)

    def confirm_code(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.CONFIRM_BUTTON)).click()

    def get_phone_value(self):
        """Obtiene el valor actual del campo de teléfono."""
        phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.PHONE_INPUT))
        return phone_input.get_attribute("value")  # Devuelve el número ingresado


        # 4 Prueba que verifica que se agrega la tarjeta

    def add_card(self, card_number, card_code):

            payment_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PAYMENT_METHOD_BUTTON))
            payment_button.click()

            # Hacer clic en "Agregar tarjeta"
            add_card_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_BUTTON))
            add_card_button.click()

            # Ingresar el número de tarjeta
            card_number_input = self.wait.until(EC.presence_of_element_located(UrbanRoutesLocators.CARD_NUMBER_INPUT))
            card_number_input.send_keys(card_number)

            # Ingresar el código CVV
            card_code_input = self.wait.until(EC.presence_of_element_located(UrbanRoutesLocators.CARD_CODE_INPUT))
            card_code_input.send_keys(card_code)

            # Hacer clic en "Agregar"
            add_button = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.ADD_CARD_SUBMIT_BUTTON))
            add_button.click()

            # Cerrar el modal
            close_button = self.wait.until(EC.presence_of_element_located(UrbanRoutesLocators.CLOSE_CARD_WINDOW_BUTTON))
            self.driver.execute_script("arguments[0].click();", close_button)

     # 5 Prueba que verifica que se envia mensaje al conductor

    def enter_driver_message(self, message):
        # Hacer clic en el label para activar el campo
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(UrbanRoutesLocators.MESSAGE_LABEL)).click()

        # Escribir el mensaje en el campo de entrada
        message_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.MESSAGE_INPUT))
        message_input.clear()
        message_input.send_keys(message)

     # 6 Prueba que verifica que se pide la manta y los pañuelos

    def request_blanket_tissues(self):
        # Hacer clic en la etiqueta para seleccionar la opción
        blanket_label = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.BLANKET_TISSUE_LABEL))
        blanket_label.click()

        # Activar el interruptor (si no está activado)
        switch = self.wait.until(EC.presence_of_element_located(UrbanRoutesLocators.BLANKET_TISSUE_SWITCH))
        if not switch.is_selected():  # Verificar si ya está activado
         self.driver.execute_script("arguments[0].click();", switch)

     # 7 Prueba que verifica que se pide los dos helados

    def request_two_ice_creams(self):
        plus_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ICE_CREAM_PLUS_BUTTON))
        plus_button.click()
        time.sleep(1)  # Pequeño delay en caso de animación
        plus_button.click()

     # 8 Prueba que verifica que reserva el taxi

    def reserve_taxi(self):
        reserve_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.RESERVE_TAXI_BUTTON))
        reserve_button.click()
        modal = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UrbanRoutesLocators.MODAL_VISIBLE))



