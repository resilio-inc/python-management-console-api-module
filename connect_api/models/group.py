from .base_model import BaseModel


class Group(BaseModel):
    def __init__(self, api, data):
        super(Group, self).__init__(api, data)

    def __str__(self):
        return '{}'.format(self._attrs['name'])

    def save(self):
        if not self.created:
            model_id = self._create_group(self._attrs)
            self._attrs['id'] = model_id
        else:
            self._update_group(self._attrs)
        self.fetch()

    def fetch(self):
        self._attrs = self._get_group(self.id)
