import basePages
from locators.locators import Home


class HomePages(basePages.BasePage):
    def load(self):
        elemLoad=self.driver.find_element(*Home.elemLoad)
        self.mouse_click(elemLoad)