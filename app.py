import requests
from pages.books_pages import BooksPages
from time import perf_counter


BASE_URL = "https://books.toscrape.com/"

books_content = requests.get(BASE_URL).content

page = BooksPages(books_content)

lower_limit, upper_limit = page.allBooksPage

_books = []

print("LOADING DATA ......")
# for i in range(int(lower_limit),int(upper_limit)+1):
for i in range(1,10):
    current_time = perf_counter()
    base_page_url = "https://books.toscrape.com/catalogue/page-{}.html".format(i)
    books_content = requests.get(base_page_url).content
    page = BooksPages(books_content)
    _books.extend(page.books)
    # print("Time Taken ----> ", perf_counter()-current_time)
print("LOADING DATA FINSHED....")
# print(_books)

# for book in page.books:
#     print("TITILE -> ",book.title)
#     print("RATING -> ",book.rating)
#     print("PRICE ->",book.price)
#     print("IMAGE ->",book.image)
#     print("-"*50)