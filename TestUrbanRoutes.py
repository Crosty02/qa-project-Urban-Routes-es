import time
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from UrbanRoutesPage import UrbanRoutesPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from localizadores.Urban_Routes_Locators import UrbanRoutesLocators


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    # 1 Confirmación del establecimiento de la ruta

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # 2 Prueba que verifica que se selecciona la tarifa Comfort

    def test_set_route_and_select_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()

        time.sleep(2)  # Espera para la carga de las tarifas

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        assert routes_page.is_comfort_selected(), "Error: La tarifa Comfort no fue seleccionada correctamente."


    # 3 Prueba que verifica que se agrega el número de teléfono y el código de confirmation

    def test_set_route_and_verify_phone(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()
        time.sleep(2)

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        time.sleep(2)

        # Rellenar número de teléfono
        routes_page.enter_phone_number(data.phone_number)
        time.sleep(1)

        # Hacer clic en "Siguiente"
        routes_page.click_next()
        time.sleep(5)

        # Ingresar el código de verificación
        routes_page.enter_verification_code()
        time.sleep(1)

        # Confirmar código
        routes_page.confirm_code()

        # Verificar que el número de teléfono ingresado es correcto
        phone_value = routes_page.get_phone_value()
        assert phone_value == data.phone_number, f"Error: Se ingresó '{phone_value}', pero se esperaba '{data.phone_number}'."

    # 4 Prueba que verifica que se agrega la tarjeta

    def test_add_card(self):
            """Prueba para agregar una tarjeta después de validar el número."""
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)

            # Ingresar direcciones
            address_from = data.address_from
            address_to = data.address_to
            routes_page.set_from(address_from)
            routes_page.set_to(address_to)

            time.sleep(2)  # Espera corta para asegurar que los valores se ingresen correctamente

            # Hacer clic en "Pedir un taxi"
            routes_page.request_taxi()
            time.sleep(2)

            # Seleccionar tarifa Comfort
            routes_page.select_comfort_tariff()
            time.sleep(2)

            # Rellenar número de teléfono
            routes_page.enter_phone_number(data.phone_number)
            time.sleep(1)

            # Hacer clic en "Siguiente"
            routes_page.click_next()
            time.sleep(5)

            # Ingresar el código de verificación
            routes_page.enter_verification_code()
            time.sleep(1)

            # Confirmar código
            routes_page.confirm_code()

            #  Agregar tarjeta
            routes_page.add_card(data.card_number, data.card_code)

            #  Verificar que la tarjeta se agregó correctamente
            card_confirmation_element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(UrbanRoutesLocators.CARD_ADDED_CONFIRMATION),
            "⚠ Error: El texto de confirmación de la tarjeta no apareció a tiempo.")

            assert card_confirmation_element.text == "Tarjeta", \
            f"⚠ Error: Se esperaba 'Tarjeta', pero se encontró: {card_confirmation_element.text}"


    # 5 Prueba que verifica que se envia mensaje al conductor

    def test_set_route_add_card_and_message(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()
        time.sleep(2)

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        time.sleep(2)

        # Rellenar número de teléfono
        routes_page.enter_phone_number(data.phone_number)
        time.sleep(1)

        # Hacer clic en "Siguiente"
        routes_page.click_next()
        time.sleep(5)

        # Ingresar el código de verificación
        routes_page.enter_verification_code()
        time.sleep(1)

        # Confirmar código
        routes_page.confirm_code()

        message = data.message_for_driver
        routes_page.enter_driver_message(message)
        time.sleep(1)

        # Verificar que el mensaje se ingresó correctamente usando el localizador correcto
        message_input = self.driver.find_element(*UrbanRoutesLocators.MESSAGE_INPUT)
        assert message_input.get_attribute("value") == message, \
        f"⚠ Error: Se esperaba '{message}', pero el campo contiene '{message_input.get_attribute('value')}'."

    # 6 Prueba que verifica que se pide la manta y los pañuelos

    def test_request_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()
        time.sleep(2)

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        time.sleep(2)

        # Rellenar número de teléfono
        routes_page.enter_phone_number(data.phone_number)
        time.sleep(1)

        # Hacer clic en "Siguiente"
        routes_page.click_next()
        time.sleep(5)

        # Ingresar el código de verificación
        routes_page.enter_verification_code()
        time.sleep(1)

        # Confirmar código
        routes_page.confirm_code()

        #  Pedir Manta y Pañuelos
        routes_page.request_blanket_tissues()
        time.sleep(1)

        # Validación: Verificar que el interruptor está activado
        switch = self.driver.find_element(*UrbanRoutesLocators.BLANKET_TISSUE_SWITCH)
        assert switch.is_selected()

    # 7 Prueba que verifica que se pide los dos helados

    def test_request_two_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()
        time.sleep(2)

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        time.sleep(2)

        # Rellenar número de teléfono
        routes_page.enter_phone_number(data.phone_number)
        time.sleep(1)

        # Hacer clic en "Siguiente"
        routes_page.click_next()
        time.sleep(5)

        # Ingresar el código de verificación
        routes_page.enter_verification_code()
        time.sleep(1)

        # Confirmar código
        routes_page.confirm_code()

        # Pedir 2 Helados
        routes_page.request_two_ice_creams()
        time.sleep(2)

        #  Verificar que la cantidad de helados es 2 y que el localizador es correcto
        ice_cream_count_element = self.driver.find_element(*UrbanRoutesLocators.ICE_CREAM_COUNT)
        ice_cream_count = ice_cream_count_element.text.strip()
        assert ice_cream_count == "2", f"⚠ Error: Se esperaban 2 helados, pero el contador muestra '{ice_cream_count}'."


    # 8 Prueba que verifica que reserva el taxi modal

    def test_reserve_taxi_modal(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()

        # Rellenar número de teléfono

        routes_page.enter_phone_number(data.phone_number)

        # Hacer clic en "Siguiente"
        routes_page.click_next()

        # Ingresar el código de verificación
        routes_page.enter_verification_code()

        # Confirmar código
        routes_page.confirm_code()

        routes_page.request_route_and_verify_modal()

        # Verificar que el modal sea visible
        modal = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'order-header-title') and text()='Buscar automóvil']"))
     ,"El modal con el título 'Buscar automóvil' no apareció.")
        assert modal.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
