from flask import render_template, redirect, url_for, request, Flask
from app.service.book_service import BookService

ui = Flask(__name__, template_folder="../../templates", static_folder="../../../resources/static")

prefix_string = "/rest/api/ui"

@ui.route(f"/")
def home():
    return render_template('index.html')

@ui.route(f"{prefix_string}/books", methods=['GET'])
def book_list():
    service = BookService()
    books = service.get_all_books() 
    return render_template('book_list.html', books=books)

@ui.route(f"{prefix_string}/books/add", methods=['GET', 'POST'])
def add_book():
    service = BookService()

    if request.method == 'POST':
        book = {
            "id": len(service.get_all_books()) + 1, 
            "title": request.form['title'],
            "author": request.form['author'],
            "published_date": request.form['published_date'],
        }

        service.create_book(book)
        return redirect(url_for('ui.book_list')) 
    return render_template('add_book.html')