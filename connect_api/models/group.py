from .base_model import BaseModel


class Group(BaseModel):
    def __init__(self, api, data):
        super().__init__(api, data)

    def __str__(self):
        return '{}'.format(self._attrs['name'])

    def save(self):
        if not self.created:
            self._attrs = self._create_group(self._attrs)
        else:
            self._attrs = self._update_group(self._attrs)

    def fetch(self):
        self._attrs = self._get_group(self.id)
