from hashlib import pbkdf2_hmac


class Link:
    def __init__(self, id, url, autodelete, password):
        self.id = id
        self.url = url
        self.autodelete = autodelete
        self.hashed_password = Link._hash_password(id, url, autodelete, password)
        self.visits = 0
        self.db_id = None

    @staticmethod
    def _hash_password(id, url, autodelete, password):
        return pbkdf2_hmac('sha256', password.encode('utf-8'), id.encode('utf-8'), 100000)

    def check_password(self, password):
        return Link._hash_password(self.id, self.url, self.autodelete, password)\
            == self.hashed_password