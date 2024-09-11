from flask import Flask,request
from datetime import datetime
app = Flask(__name__)

books=[
    {
        "author": "xyz",
        "id": 1,
        "name": "Math",
        "publishAt": "Thu, 12 Sep 2024 01:40:52 GMT"
    },
    {
        "author": "abc",
        "id": 2,
        "name": "Eng",
        "publishAt": "Thu, 12 Sep 2024 01:41:01 GMT"
    },
    {
        "author": "abc",
        "id": 3,
        "name": "Eng",
        "publishAt": "Thu, 12 Sep 2024 01:41:01 GMT"
    }
    
]

# add new book endpoint 
@app.route('/books/', methods=['POST'])
def add_book():
    body = request.get_json()
    name = body['name']
    author = body['author']
    id = len(books) + 1
    createdAt = datetime.today()
    bookObj ={
        "name":name,
        "author":author,
        "id":id,
        "publishAt":createdAt
    }
    books.append(bookObj)
    return {
        "message":'New book added successfully',
        "book": bookObj
    }

# fetching all books 
@app.route('/books/', methods=['GET'])
def get_books():
    return {
        "message":'fetched successfully',
        "books": books
    }

# fetching book by id 
@app.route('/books/<id>', methods=['GET'])
def get_single_book(id):
    try:
        book_id = int(id)
    except ValueError:
        return {
            "message": "Invalid book ID."
        }
        
    filtered_book = next((book for book in books if book['id']==book_id), None)
    if(filtered_book):
        return {
        "message":'fetched successfully',
        "books": filtered_book
    }
    else:
        return {
            "message": f"Book with ID {id} not found."
        }


# update book endpoint 
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    body = request.get_json()
    
    try:
        book_id = int(id)
    except ValueError:
        return {
            "message": "Invalid book ID."
        }
    is_valid_id = next((book for book in books if book['id']==book_id),None)
    
    if(is_valid_id):
        is_valid_id['name'] = body['name']
        print(is_valid_id)
        return {
        "message":'updated book successfully',
        "books": is_valid_id
    }
    else:
      return {
            "message": f"Book with ID {id} not found."
     }



# delete endpoint 
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    try:
        book_id = int(id)
    except ValueError:
        return {
            "message": "Invalid book ID."
        }
    # books = [book for book in books if book['id'] != book_id]
    is_valid_id = next((book for book in books if book['id']==book_id),None)
    # print(is_valid_id)
    if(is_valid_id):
        books.remove(is_valid_id)
        return {
        "message":'deleted successfully',
        "books": books
    }
    else:
      return {
            "message": f"Book with ID {id} not found."
     }



app.run(
    debug=True,
    port=8000
)