from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ElectronicPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _page_title = (By.XPATH, "//div[@class='page-title']//h1")
