from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from bson import ObjectId

@dataclass
class BookRequest:
    title: Optional[str] = None
    author_id: Optional[ObjectId] = None
    genre: Optional[str] = None
    yearPublished: Optional[datetime] = None