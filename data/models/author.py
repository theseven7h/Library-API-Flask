from dataclasses import dataclass
from typing import Optional

from bson.objectid import ObjectId

@dataclass
class Author:
    author_id: Optional[ObjectId] | str = None
    name: str = None
    bio: str = None

    def to_dict(self):
        data = {
            'name': self.name,
            'bio': self.bio
        }
        if self.author_id:
            data['_id'] = self.author_id
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            author_id= str(data.get('_id')),
            name = data.get('name'),
            bio = data.get('bio')
        )