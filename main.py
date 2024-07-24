from app import _books

def sorting_by_price(book=_books, reverse=True):
    return sorted(book, key=lambda x: x.price, reverse=reverse)

def top_ten_book(book=_books):
    return sorted(book, key=lambda x: x.price, reverse=True)[:10]

def high_price_book(book=_books):
    return sorted(book, key=lambda x: x.price, reverse=True)[:1]

def high_rated_top_ten(book = _books):
    return sorted(book, key=lambda x: x.rating, reverse=True)[:10]


def beautify(result):
    print("+"+'-'*100+"+"+"-"*15+"+"+"-"*10+"+")
    # print("|{:<100}|{:<15}|{:<10}|".format('TITLE', 'PRICE', 'RATING'))
    print("|{:^100}|{:^15}|{:^10}|".format('TITLE', 'PRICE', 'RATING'))
    print("+"+'-'*100+"+"+"-"*15+"+"+"-"*10+"+")
    for res in result:
        print("|{:<100}|{:<15}|{:<10}|".format(res.title, res.price,res.rating))
        print("+"+'-'*100+"+"+"-"*15+"+"+"-"*10+"+")


def main():
    menu = '''
    1. Sort with Price
    2. Get top 10 high rated books
    3. High price books
    4. High rated top 10 Books
    5. exit or any other
    '''
    fun_list = {
        1: sorting_by_price,
        2: top_ten_book,
        3: high_price_book,
        4: high_rated_top_ten
    }
    while True:
        print(menu)
        try:
            i = int(input("Enter you input:"))
            if i not in fun_list.keys():
                break
            else:
                RESULT = fun_list[i]()
                beautify(RESULT)
        except ValueError as e:
            print("Please Enter only integer Value b/w 1 to 5.")
        


if __name__ == "__main__":
    # result = sorting_by_price()
    # print(result)
    main()
