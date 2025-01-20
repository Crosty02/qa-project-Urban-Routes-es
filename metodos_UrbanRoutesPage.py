from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from localizadores.urban_routes_locators import UrbanRoutesLocators

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_route(self, from_address, to_address):
        """Ingresa la dirección de origen y destino"""
        from_field = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.FROM_FIELD))
        to_field = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.TO_FIELD))
        from_field.send_keys(from_address)
        to_field.send_keys(to_address)

    def select_comfort_tariff(self):
        """Selecciona la tarifa Comfort"""
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF)).click()

    def enter_phone_number(self, phone):
        """Ingresa el número de teléfono"""
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.PHONE_INPUT)).send_keys(phone)

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
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.MESSAGE_INPUT)).send_keys(message)

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

