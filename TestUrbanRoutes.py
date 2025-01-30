import time
import data
from UrbanRoutesPage import UrbanRoutesPage
from localizadores.Urban_Routes_Locators import UrbanRoutesLocators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestUrbanRoutes:
    driver = None

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

        time.sleep(2)  # Espera corta para asegurar que los valores se ingresen correctamente
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # Hacer clic en "Pedir un taxi"
        routes_page.request_taxi()

        time.sleep(2)  # Espera para la carga de las tarifas

        # Seleccionar tarifa Comfort
        routes_page.select_comfort_tariff()

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

    def test_set_route_and_add_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Ingresar direcciones
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)

        time.sleep(2)

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
        time.sleep(2)

        # Agregar Tarjeta de Crédito
        routes_page.open_payment_method()
        time.sleep(1)

        routes_page.add_card()
        time.sleep(1)

        routes_page.enter_card_details(data.card_number, data.card_code)
        # time.sleep(1)

        routes_page.submit_card()
        time.sleep(2)

        # Cerrar modal
        routes_page.close_card_modal()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()