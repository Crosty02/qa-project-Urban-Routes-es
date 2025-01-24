from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from localizadores.Urban_Routes_Locators import UrbanRoutesLocators


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def set_route(self, address_from, address_to ):
        self.driver.find_element(*UrbanRoutesLocators.FROM_FIELD).click()
        self.driver.find_element(*FROM_FIELD).send_keys("from_address")
        self.driver.find_element(By.TO_FIELD,"to_address").click()
        self.driver.find_element(By.TO_FIELD).send_keys("to_address")


    def select_comfort_tariff(self):
        """Selecciona la tarifa Comfort"""
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF)).click()

    def enter_phone_number(self, phone):
        """Ingresa el número de teléfono"""
        phone_input = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.PHONE_INPUT))
        phone_input.send_keys(phone)

    def add_credit_card(self, card_number, cvv, retrieve_phone_code):
        """Añade una tarjeta de crédito y confirma el código de seguridad"""
        # Hacer clic en el botón "Agregar tarjeta"
        self.driver.find_element(*UrbanRoutesLocators.ADD_CARD_BUTTON).click()

        # Ingresar el CVV
        cvv_input = self.driver.find_element(*UrbanRoutesLocators.CVV_INPUT)
        cvv_input.send_keys(cvv)

        # Simular que el usuario presiona TAB para perder el enfoque
        cvv_input.send_keys(Keys.TAB)

        # Confirmar la tarjeta haciendo clic en "link"
        link_button = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.LINK_BUTTON))
        link_button.click()

        # Simular la recepción del código de confirmación
        code = retrieve_phone_code()
        return code

    def send_message(self, message):
        """Envía un mensaje al conductor"""
        message_input = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.MESSAGE_INPUT))
        message_input.send_keys(message)

    def request_blanket_and_tissues(self):
        """Solicita una manta y pañuelos"""
        self.driver.find_element(*UrbanRoutesLocators.BLANKET_CHECKBOX).click()
        self.driver.find_element(*UrbanRoutesLocators.TISSUES_CHECKBOX).click()

    def request_ice_cream(self, quantity=2):
        """Solicita la cantidad especificada de helados"""
        for _ in range(quantity):
            self.driver.find_element(*UrbanRoutesLocators.ICE_CREAM_PLUS_BUTTON).click()

    def wait_for_taxi_search_modal(self):
        """Espera a que aparezca el modal de búsqueda de taxi"""
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.SEARCH_TAXI_MODAL))

    def wait_for_driver_info(self):
        """Espera a que aparezca la información del conductor"""
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.DRIVER_INFO))

    # Métodos auxiliares para validar datos en las pruebas
    def get_address_from(self):
        """Obtiene la dirección de origen ingresada"""
        return self.driver.find_element(*UrbanRoutesLocators.FROM_FIELD).get_attribute("value")

    def get_address_to(self):
        """Obtiene la dirección de destino ingresada"""
        return self.driver.find_element(*UrbanRoutesLocators.TO_FIELD).get_attribute("value")

    def is_comfort_selected(self):
        """Verifica si la tarifa Comfort está seleccionada"""
        return "selected" in self.driver.find_element(*UrbanRoutesLocators.COMFORT_TARIFF).get_attribute("class")

    def get_phone_number(self):
        """Obtiene el número de teléfono ingresado"""
        return self.driver.find_element(*UrbanRoutesLocators.PHONE_INPUT).get_attribute("value")

    def get_sent_message(self):
        """Obtiene el mensaje enviado al conductor"""
        return self.driver.find_element(*UrbanRoutesLocators.MESSAGE_INPUT).get_attribute("value")

    def is_blanket_selected(self):
        """Verifica si la opción de frazada está seleccionada"""
        return self.driver.find_element(*UrbanRoutesLocators.BLANKET_CHECKBOX).is_selected()

    def get_ice_cream_count(self):
        """Cuenta cuántos helados se han agregado"""
        return int(self.driver.find_element(*UrbanRoutesLocators.ICE_CREAM_PLUS_BUTTON).get_attribute("value"))

    def get_taxi_search_modal_visible(self):
        """Verifica si el modal de búsqueda de taxi está visible"""
        return self.driver.find_element(*UrbanRoutesLocators.SEARCH_TAXI_MODAL).is_displayed()


