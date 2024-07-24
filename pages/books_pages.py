import bs4


from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocator
from parsers.books import BooksParser
from utils.extract import pageRange

class BooksPages:
    def __init__(self, page) -> None:
        self.soupe = BeautifulSoup(page, 'html.parser')
    
    @property
    def books(self):
        locator = BooksPageLocator.BOOKS
        books_tags = self.soupe.select(locator)
        return [BooksParser(e) for e in books_tags]

    # @property
    # def menu(self):
    #     locator = BooksPageLocator.MENU
    #     books_menu = self.soupe.select(locator)
    #     return books_menu

    @property
    def allBooksPage(self):
        locator = BooksPageLocator.PAGE
        pages = self.soupe.select_one(locator).string
        limit = pageRange(pages)
        return limit