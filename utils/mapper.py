from data.models.author import Author
from dto.requests.add_author_request import AuthorRequest
from dto.responses.AddAuthorResponse import AddAuthorResponse


class Mapper:
    @staticmethod
    def map_to_author(request: AuthorRequest):
        return Author(
            name = request.name,
            bio = request.bio
        )

    @staticmethod
    def map_to_response(saved_author):
        return AddAuthorResponse(
            author_id = saved_author.author_id,
            name = saved_author.name,
            bio = saved_author.bio
        )