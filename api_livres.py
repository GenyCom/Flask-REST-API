"""
Created on : 01-10-2024 by Abdelali EL AMRANI
subject : REST API développé en Flask 
Details : without secure KEY
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de données simulée
books = [
    {"id": 1, "title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "1987", "author": "Gergino"},
    {"id": 4, "title": "2002", "author": "alpa"},
    {"id": 5, "title": "man on the fire", "author": "Diensel"},
]

# recuperer la liste des books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# recuperer un livre
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Livre non trouvé"}), 404

# add book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = max(book['id'] for book in books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# main methods
if __name__ == "__main__":
    app.run(debug=True)
    
