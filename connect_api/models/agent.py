from .base_model import BaseModel


class Agent(BaseModel):
    def __init__(self, api, data):
        super().__init__(api, data)

    def __str__(self):
        return '{}[{}]'.format(self._attrs['name'], self._attrs['ip'])

    def fetch(self):
        self._attrs = self._get_agent(self.id)