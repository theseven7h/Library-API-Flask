from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from bson import ObjectId

@dataclass
class Book:
    book_id: Optional[ObjectId | str] = None
    title: Optional[str] = None
    author_id: Optional[ObjectId] = None
    genre: Optional[str] = None
    yearPublished: Optional[datetime] = None

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
        return cls(
            book_id = str(data.get('_id')),
            title = data.get('title'),
            author_id = data.get('author_id'),
            genre = data.get('genre'),
            yearPublished = data.get('year_published')
        )
