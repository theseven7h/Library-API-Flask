from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorRequest:
     name: Optional[str]
     bio: Optional[str]