from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorRequest:
     name: Optional[str] = None
     bio: Optional[str] = None