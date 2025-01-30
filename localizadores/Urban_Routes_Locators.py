from selenium.webdriver.common.by import By
class UrbanRoutesLocators:
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    REQUEST_TAXI_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Pedir un taxi')]")
    COMFORT_TARIFF = (By.XPATH, "//div[contains(@class, 'card-title') and text()='Comfort']")
    PHONE_FIELD_LABEL = (By.XPATH, "//div[contains(@class, 'np-text') and text()='Número de teléfono']")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Siguiente')]")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Confirmar')]")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'pp-text') and text()='Método de pago']")
    ADD_CARD_BUTTON = (By.XPATH, "//div[contains(@class, 'pp-title') and text()='Agregar tarjeta']")
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CVV_INPUT = (By.ID, "code")
    CARD_PLC_IMAGE =(By.XPATH,"//div[contains(@class, 'pp-buttons')]/button[contains(@class, 'full') and text()='Agregar']")
    ADD_CARD_SUBMIT = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Agregar')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'close-button')]")



