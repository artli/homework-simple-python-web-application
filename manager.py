import shelve


class Manager:
    def __init__(self, db_path):
        self._db = shelve.open(db_path)

    def get_all_links(self):
        entries = []
        for db_id, link in self._db.items():
            link.db_id = int(db_id)
            entries.append(link)
        return sorted(entries, key=lambda e: e.db_id)

    def get_filtered(self, predicate):
        return list(filter(predicate, self.get_all_links()))

    def get_link_by_id(self, link_id):
        filtered = self.get_filtered(lambda link: link.id == link_id)
        if filtered:
            return filtered[0]
        return None

    def save(self, link):
        old_link = self.get_link_by_id(link.id)
        if old_link:
            db_id = str(old_link.db_id)
        else:
            db_id = str(max((int(key) + 1 for key in self._db.keys()), default=0))
        link.db_id = db_id
        self._db[db_id] = link
        self._db.sync()

    def delete(self, link):
        if link.db_id is not None:
            del self._db[str(link.db_id)]
            self._db.sync()
            return True
        return False