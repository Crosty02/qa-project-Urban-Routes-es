from selenium.webdriver.common.by import By
class UrbanRoutesLocators:
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    REQUEST_TAXI_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Pedir un taxi')]")
    COMFORT_TARIFF = (By.XPATH, "//div[contains(@class, 'card') and .//div[text()='Comfort']]")
    PHONE_FIELD_LABEL = (By.XPATH, "//div[contains(@class, 'np-text') and text()='Número de teléfono']")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Siguiente')]")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Confirmar')]")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[contains(@class, 'pp-text') and text()='Método de pago']")
    ADD_CARD_BUTTON = (By.XPATH, "//div[contains(@class, 'pp-title') and text()='Agregar tarjeta']")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@id='number' and @name='number']")
    CARD_CODE_INPUT = (By.XPATH, "//input[@id='code' and @name='code']")
    ADD_CARD_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'button full') and text()='Agregar']")
    CLOSE_CARD_WINDOW_BUTTON = (By.XPATH, "//button[contains(@class, 'close-button section-close')]")
    CARD_ADDED_CONFIRMATION = (By.XPATH, "//div[contains(@class, 'pp-value-text') and text()='Tarjeta']")
    EMPTY_SPACE = (By.XPATH, "//div[@class='pp-buttons']")
    MESSAGE_LABEL = (By.XPATH, "//label[@for='comment']")
    MESSAGE_INPUT = (By.XPATH, "//input[@id='comment' and @name='comment']")
    BLANKET_TISSUE_LABEL = (By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Manta y pañuelos']")
    BLANKET_TISSUE_SWITCH = (By.XPATH, "//div[contains(@class, 'r-sw')]//input[@type='checkbox']")
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, "//div[contains(@class, 'counter-plus')]")
    ICE_CREAM_COUNT = (By.XPATH, "//div[contains(@class, 'counter-value')]")
    REQUEST_ROUTE_BUTTON = (By.XPATH,"//span[contains(@class, 'smart-button-secondary') and contains(text(), 'El recorrido será de 1 kilómetros')]")
    ORDER_TITLE_MODAL = (By.XPATH, "//div[contains(@class, 'order-header-title') and text()='Buscar automóvil']")
