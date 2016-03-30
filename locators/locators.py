from selenium.webdriver.common.by import By


class baseLocators():
    pass

class Home(baseLocators):
    elemLoad=(By.XPATH,"//input[@id='Load']")

class Table(baseLocators):
    elemTable=(By.XPATH,"//table[@id='VIPs']")
    elemRadio=(By.XPATH,"//input[@id='VIP']")