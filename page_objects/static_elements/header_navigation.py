from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By

from page_objects.apparel_shoes_page import ApparelShoesPage
from page_objects.books_page import BooksPage
from page_objects.computer_page import ComputerPage
from page_objects.digital_page import DigitalPage
from page_objects.electronic_page import ElectronicPage
from page_objects.jewerly_page import JewerlyPage
from page_objects.gift_cards_page import GiftCardPage


class HeaderNavigation(ABC):
    _urls = {
        'books_url': (By.XPATH, "//ul[@class='top-menu']//a[contains(text(), 'Books')]"),
        'computers_url': (By.XPATH, "//ul[@class='top-menu']//a[contains(text(), 'Computers')]"),
        'desktops_url': (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']//ul[@class='sublist firstLevel']"
                                   "//li//a[contains(text(), 'Desktops')]"),
        'electronics_url': (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']//li"
                                      "//a[@href='/electronics']"),
        'apparel_shoes_url': (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']"
                                        "//li//a[@href='/apparel-shoes']"),
        'digital_url': (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']//li"
                                  "//a[@href='/digital-downloads']"),
        'jewerly_url': (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']//li//a[@href='/jewelry']"),
        'gift_cards': (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']//li//a[@href='/gift-cards']")
    }

    _pages = {
        'books_url': BooksPage,
        'computers_url': ComputerPage,
        'electronics_url': ElectronicPage,
        'apparel_shoes_url': ApparelShoesPage,
        'digital_url': DigitalPage,
        'jewerly_url': JewerlyPage,
        'gift_cards': GiftCardPage
    }

    @abstractmethod
    def get_navigation_link(self, url): ...
    """
    Method allows to make a click on link or receive it`s text value.
    
    :param url: Element locator according to _urls dictionary
    :param result: Action for method: can be "click" or "text"
    :return: Returns a text of object or new page object
    """
