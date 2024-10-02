"""
Created on : 01-10-2024 by Abdelali EL AMRANI
subject : REST API développé en Flask 
Details : with secure method
"""


from flask import Flask, jsonify, request, abort
from functools import wraps

app = Flask(__name__)

# Clé API simulée (dans un cas réel, vous la stockeriez de manière sécurisée)
API_KEY = "@abdo"

# Liste de livres (comme avant)
books = [
    {"id": 1, "title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-Key') and request.headers.get('X-API-Key') == API_KEY:
            return view_function(*args, **kwargs)
        else:
            abort(401)  # Unauthorized
    return decorated_function

@app.route('/books', methods=['GET'])
@require_api_key
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
@require_api_key
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Livre non trouvé"}), 404

@app.route('/books', methods=['POST'])
@require_api_key
def add_book():
    new_book = request.json
    new_book['id'] = max(book['id'] for book in books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)