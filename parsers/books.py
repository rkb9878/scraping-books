from utils import extract
from locators.books_locators import BooksLocator

class BooksParser:
    RATING = {
        'One' : 1,
        'Two': 2,
        'Three': 3,
        'Four': 4, 
        'Five': 5
    }
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self) -> str:
        return f"<Books title: {self.title}, price: {self.price}, rating: {self.rating}>"
    
    @property
    def title(self):
        locator = BooksLocator.TITLE
        item = self.parent.select_one(locator)
        return item.attrs.get('title')

    @property
    def image(self):
        locator = BooksLocator.IMAGE
        item = self.parent.select_one(locator)
        return item.attrs.get('href')
    
    @property
    def rating(self):
        locator = BooksLocator.RATING
        item = self.parent.select_one(locator)
        classess = [self.RATING.get(c) for c in item.attrs.get('class') if 'star-rating'!=c]
        return classess[0]
    
    @property
    def price(self):
        locator = BooksLocator.PRICE
        item = self.parent.select_one(locator).string
        return float(extract.fetch_amount_from_string(item)[0])

    
