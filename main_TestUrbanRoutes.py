import pytest
from setup_driver import setup_driver
from metodos_UrbanRoutesPage import UrbanRoutesPage
from data import urban_routes_url, address_from, address_to

@pytest.fixture(scope="class")
def driver():
    driver = setup_driver()
    driver.get(urban_routes_url)
    yield driver
    driver.quit()

class TestUrbanRoutes:
    def test_set_route(self, driver):
        routes_page = UrbanRoutesPage(driver)
        routes_page.set_route(address_from, address_to)

    class TestUrbanRoutes:

        def test_order_taxi(self, driver):
            """Prueba el flujo completo de pedir un taxi"""
            routes_page = UrbanRoutesPage(driver)

            # Paso 1: Configurar las direcciones
            routes_page.set_route(address_from, address_to)

            # Paso 2: Seleccionar la tarifa Comfort
            routes_page.select_comfort_tariff()

            # Paso 3: Rellenar el número de teléfono
            routes_page.enter_phone_number("+1234567890")

            # Paso 4: Agregar tarjeta de crédito (Consejo aplicado aquí)
            routes_page.add_credit_card("4111111111111111", "123")

            # Paso 5: Enviar un mensaje al conductor
            routes_page.send_message("Por favor, maneje con cuidado.")

            # Paso 6: Pedir una manta y pañuelos
            routes_page.request_blanket_and_tissues()

            # Paso 7: Pedir 2 helados
            routes_page.request_ice_cream()

            # Paso 8: Esperar a que aparezca el modal de búsqueda de taxi
            routes_page.wait_for_taxi_search_modal()

            # Paso 9: (Opcional) Esperar a que aparezca la información del conductor
            routes_page.wait_for_driver_info()

