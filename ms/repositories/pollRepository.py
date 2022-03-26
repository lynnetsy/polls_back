from ms.models import Poll
from .repository import Repository

class PollRepository(Repository):
    def get_model(self):
        return Poll

    def add(self, data):
        poll = self._model(data)
        self.db_save(poll)
        return poll
    