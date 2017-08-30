from .base_model import BaseModel


class Agent(BaseModel):
    def __init__(self, api, data):
        super(Agent, self).__init__(api, data)

    def __str__(self):
        return '{}[{}]'.format(self._attrs['name'], self._attrs['ip'])

    def fetch(self):
        self._attrs = self._get_agent(self.id)

    @property
    def name(self):
        return self._attrs['name']

    @property
    def deviceid(self):
        return self._attrs['deviceid']

    @property
    def online(self):
        return self._attrs['online']

    @property
    def ip(self):
        if 'ip' not in self._attrs:
            return None
        return self._attrs['ip']

