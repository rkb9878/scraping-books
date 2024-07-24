from flask import Flask, request
from main import sorting_by_price, top_ten_book, high_price_book, high_rated_top_ten, _books
import sys
from flask_cors import CORS

app  = Flask(__name__)
CORS(app)

def formate_json(obj):
    json = []
    for i in obj:
        dist = {
            'title': i.title,
            'price': i.price,
            'rating': i.rating
        }
        json.append(dist)
    return json

@app.get('/')
def get_all_data(sortbyprice=False):
    if sortbyprice:
        all_book = formate_json(sorting_by_price)        
    else:
        all_book = formate_json(_books)
    return all_book

@app.get('/top-ten')
def get_top_ten_books():
    print(request.args, file=sys.stderr)
    if request.args.get('rating'):
        book = formate_json(high_rated_top_ten())
    else:
        book = formate_json(top_ten_book())
    return book




# if __name__=="__main__":
#     app.run()