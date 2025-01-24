import pytest
from setup_driver import setup_driver
from UrbanRoutesPage import UrbanRoutesPage
from data import urban_routes_url, address_from, address_to
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.get(urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)



    def test_set_route(self):
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_address_from() == address_from
        assert self.routes_page.get_address_to() == address_to

    def test_set_comfort(self):
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.is_comfort_selected()

    def test_set_phone_number(self):
        self.routes_page.enter_phone_number("+1 123 123 12 12")
        assert self.routes_page.get_phone_number() == "+1 123 123 12 12"

    def test_add_card(self):
        self.routes_page.add_credit_card("1234 5678 9100", "111")
        assert self.routes_page.add_credit_card()

    def test_write_message(self):
        self.routes_page.send_message("Muéstrame el camino al museo")
        assert self.routes_page.get_sent_message() == "Muéstrame el camino al museo"

    def test_blanket(self):
        self.routes_page.request_blanket_and_tissues()
        assert self.routes_page.is_blanket_selected()

    def test_add_icecream(self):
        self.routes_page.request_ice_cream(quantity=2)
        assert self.routes_page.get_ice_cream_count() == 2

    def test_find_driver(self):
        self.routes_page.wait_for_taxi_search_modal()
        assert self.routes_page.get_taxi_search_modal_visible()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()