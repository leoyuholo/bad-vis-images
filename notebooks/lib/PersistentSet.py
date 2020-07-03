import simplejson as json
from pathlib import Path

class PersistentSet (set):
    @staticmethod
    def load_set (file):
        if Path(file).exists():
            s = PersistentSet([frozenset(a) if isinstance(a, list) else a for a in json.load(open(file))])
        else:
            s = PersistentSet()
        s.set_file(file)
        return s

    def set_file (self, file):
        self.file = file

    def save (self):
        json.dump(list(self), open(self.file, 'w'), iterable_as_array=True)

    def persist_add (self, item):
        self.add(item)
        self.save()

    def persist_remove (self, item):
        self.remove(item)
        self.save()
