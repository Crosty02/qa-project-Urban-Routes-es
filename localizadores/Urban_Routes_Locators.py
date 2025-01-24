from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    FROM_FIELD = (By.ID, "from_address")
    TO_FIELD = (By.ID, "to_address")
    CALL_TAXI_BUTTON = (By.ID, "call_taxi_button")
    COMFORT_TARIFF = (By.XPATH, "//button[contains(text(), 'Comfort')]")
    PHONE_INPUT = (By.ID, "phone")
    ADD_CARD_BUTTON = (By.ID, "add-card")
    CVV_INPUT = (By.ID, "code")
    LINK_BUTTON = (By.ID, "link")
    MESSAGE_INPUT = (By.ID, "message")
    BLANKET_CHECKBOX = (By.ID, "blanket")
    TISSUES_CHECKBOX = (By.ID, "tissues")
    ICE_CREAM_PLUS_BUTTON = (By.ID, "ice-cream-plus")
    SEARCH_TAXI_MODAL = (By.ID, "search-modal")
    DRIVER_INFO = (By.ID, "driver-info")


