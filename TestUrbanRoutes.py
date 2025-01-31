import time
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UrbanRoutesPage import UrbanRoutesPage
from localizadores.Urban_Routes_Locators import UrbanRoutesLocators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from verification_code import retrieve_phone_code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    # Confirmación del establecimiento de la ruta

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # Prueba que verifica que se selecciona la tarifa Comfort

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


    # Prueba que verifica que se agrega el número de teléfono y el código de confirmation

    def test_set_route_and_verify_phone(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)

        time.sleep(2)  # Espera corta para asegurar que los valores se ingresen correctamente

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

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

            # 3️⃣ Agregar tarjeta
            routes_page.add_card(data.card_number, data.card_code)

            #  Verificar que la tarjeta se agregó correctamente
            card_confirmation_element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(UrbanRoutesLocators.CARD_ADDED_CONFIRMATION),
            "⚠ Error: El texto de confirmación de la tarjeta no apareció a tiempo.")

            assert card_confirmation_element.text == "Tarjeta", \
            f"⚠ Error: Se esperaba 'Tarjeta', pero se encontró: {card_confirmation_element.text}"

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

        # Escribir mensaje para el conductor
        routes_page.enter_driver_message(data.message_for_driver)
        time.sleep(1)


    def test_request_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Pedir un taxi
        routes_page.request_taxi()
        time.sleep(2)

        #  Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        time.sleep(2)

        #  Pedir Manta y Pañuelos
        routes_page.request_blanket_tissues()
        time.sleep(1)

        # Validación: Verificar que el interruptor está activado
        switch = self.driver.find_element(*UrbanRoutesLocators.BLANKET_TISSUE_SWITCH)
        assert switch.is_selected()

    def test_request_two_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)


        # Pedir un taxi
        routes_page.request_taxi()
        time.sleep(2)

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()
        time.sleep(2)

        # Pedir 2 Helados
        routes_page.request_two_ice_creams()
        time.sleep(2)

    def test_reserve_taxi_modal(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Establecer la ruta
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        time.sleep(2)

        # Pedir un taxi
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

        # Esperar a que el modal aparezca y reservar el taxi
        routes_page.reserve_taxi()
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
