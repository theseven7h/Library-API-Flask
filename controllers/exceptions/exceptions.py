
class AppExceptions(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class AuthorNotFoundException(AppExceptions):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class BookNotFoundException(AppExceptions):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class EmptyUpdateException(AppExceptions):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

