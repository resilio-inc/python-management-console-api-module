from ..base_connection import BaseConnection
from ..error import ModelException


class BaseModel(BaseConnection):
    def __init__(self, api, data):
        super().__init__(api._address, api._token)
        self._attrs = data if data else {}

    @property
    def created(self):
        return 'id' in self._attrs

    @property
    def attrs(self):
        return self._attrs

    @property
    def id(self):
        if 'id' not in self._attrs:
            raise ModelException('Not id field. The model is not saved.')
        return self._attrs['id']