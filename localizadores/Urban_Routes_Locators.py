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
    PAYMENT_METHOD = (By.XPATH, "//div[@class='pp-text' and contains(text(), 'Método de pago')]")
    ADD_CARD_BUTTON = (By.XPATH, "//div[@class='pp-title' and contains(text(), 'Agregar tarjeta')]")
    CARD_NUMBER_INPUT = (By.ID, "number")  # Si el ID es estable, se mantiene
    CARD_CVV_INPUT = (By.ID, "code")  # Si el ID es estable, se mantiene
    ADD_CARD_SUBMIT = (By.XPATH, "//div[@class='pp-buttons']//button[contains(text(), 'Agregar')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'close-button')]")
    EMPTY_SPACE = (By.XPATH, "//div[@class='pp-buttons']")
    MESSAGE_LABEL = (By.XPATH, "//label[@for='comment' and contains(@class, 'label')]")
    MESSAGE_INPUT = (By.ID, "comment")
    BLANKET_TISSUE_LABEL = (By.XPATH, "//div[contains(@class, 'r-sw-label') and text()='Manta y pañuelos']")
    BLANKET_TISSUE_SWITCH = (By.XPATH, "//div[contains(@class, 'r-sw')]//input[@type='checkbox']")
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, "//div[contains(@class, 'counter-plus') and text()='+']")
    RESERVE_TAXI_BUTTON = (By.XPATH,"//button[contains(@class, 'smart-button')]//span[contains(text(), 'Introducir un número de teléfono y reservar')]")



