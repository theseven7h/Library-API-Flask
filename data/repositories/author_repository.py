from bson import ObjectId

from data.models.author import Author


class AuthorRepository:
    def __init__(self, db):
        self.db = db

    def save(self, author):
        return self.db.authors.insert_one(author.to_dict()).inserted_id

    def find_all(self):
        return [Author.from_dict(author) for author in self.db.authors.find()]

    def find_by_id(self, user_id):
        document = self.db.authors.find_one({'_id': ObjectId(user_id)})
        return Author.from_dict(document) if document else None

    def update(self, author_id, author):
        ready_author = self.__get_update(author)
        if not ready_author:
            return None
        self.db.authors.update_one({'_id': ObjectId(author_id)}, {'$set': ready_author})
        updated_author = self.find_by_id(author_id)
        return updated_author

    def __get_update(self, author):
        ready_author = {}
        if author.name:
            ready_author['name'] = author.name
        if author.bio:
            ready_author['bio'] = author.bio
        return ready_author

    def delete_by_id(self, user_id):
        self.db.authors.delete_one({'_id' : ObjectId(user_id)})