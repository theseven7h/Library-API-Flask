from dataclasses import dataclass
from typing import Optional

from bson import ObjectId


@dataclass
class AddAuthorResponse:
    author_id: Optional[ObjectId | str]
    name: Optional[str]
    bio: Optional[str]

    def to_dict(self):
        return self.__dict__