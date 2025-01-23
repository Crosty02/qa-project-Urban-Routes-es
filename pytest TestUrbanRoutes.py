import pytest
from setup_driver import setup_driver
from UrbanRoutesPage import UrbanRoutesPage
from data import urban_routes_url, address_from, address_to

@classmethod
def setup_class(cls):
    cls.driver = setup_driver()
    cls.driver.get(urban_routes_url)

@classmethod
def teardown_class(cls):
    # Cerrar el navegador
    cls.driver.quit()


class TestUrbanRoutes:
    def test_order_taxi(self, driver):
        self.routes_page = UrbanRoutesPage(driver)


# Confirmación del establecimiento de la ruta
    def test_set_route(self):
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from_address() == address_from
        assert self.routes_page.get_to_address() == address_to

    # Prueba que verifica que se selecciona la tarifa Comfort
    def test_set_comfort(self):
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.is_comfort_selected()

    # Prueba para agregar número de teléfono
    def test_set_phone_number(self):
        self.routes_page.enter_phone_number("+1 123 123 12 12")
        assert self.routes_page.get_phone_number()

    # Prueba que agrega tarjeta de crédito
    def test_add_card(self):
        self.routes_page.add_credit_card("1234 5678 9100", "111")
        assert self.routes_page.add_credit_card == "1234 5678 9100"

    # Prueba que verifica que se pueda enviar mensaje para el conductor
    def test_write_message(self):
        self.routes_page.send_message("Muéstrame el camino al museo")
        assert self.routes_page.get_sent_message() =="Muéstrame el camino al museo."

    # Prueba que verifica que se pueda solicitó una frazada
    def test_blanket(self):
        self.routes_page.request_blanket_and_tissues()
        assert self.routes_page.is_blanket_selected()

    # Prueba que verifica que se añadieron helados
    def test_add_icecream(self):
        self.routes_page.request_ice_cream(quantity=2)
        assert self.routes_page.get_ice_cream_count() == 2

    # Prueba que verifica la búsqueda de un conductor
    def test_find_driver(self):
        self.routes_page.wait_for_taxi_search_modal()
        assert self.routes_page.is_taxi_search_modal_visible()

# Prueba que verifica que la información del conductor se muestra correctamente después de la búsqueda (Esta prueba es opcional)
    def test_wait_driver_information(self):
        self.routes_page.wait_for_driver_info()
        assert self.routes_page.wait_for_driver_info()
