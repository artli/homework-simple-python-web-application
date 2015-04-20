class Link:
    def __init__(self, id, url, autodelete):
        self.id = id
        self.url = url
        self.autodelete = autodelete
        self.visits = 0
        self.db_id = None