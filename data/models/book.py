from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId

@dataclass
class Book:
    book_id: ObjectId | None
    title: str
    author_id: ObjectId | None
    genre: str
    yearPublished: datetime

    def to_dict(self):
        data =  {
            'title': self.title,
            'author_id': str(self.author_id),
            'genre': str(self.genre),
            'year_published': str(self.yearPublished),
        }
        if self.book_id:
            data['_id'] = self.book_id
        return data


    @classmethod
    def from_dict(cls, data):
        book_id = data.get('_id')
        return cls(
            book_id = book_id,
            title = data.get('title'),
            author_id = data.get('author_id'),
            genre = data.get('genre'),
            yearPublished = data.get('year_published')
        )