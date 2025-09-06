from bson.objectid import ObjectId

from data.models.author import Author
from data.models.book import Book


class BookRepository:
    def __init__(self, db):
        self.db = db

    def save(self, book):
        return self.db.books.insert_one(Book.from_dict(book))

    def find_all(self):
        return [Author.from_dict(author) for author in self.db.books.find()]

    def find_by_id(self, user_id):
        return Author.from_dict(self.db.authors.find_one({'_id' : ObjectId(user_id)}))

    def update_book(self, book_id, book):
        self.db.books.update_one({'_id': ObjectId(book_id)})