from .base_model import BaseModel
from ..constants import Permission, SchedulerType
from ..utils import Path


class Job(BaseModel):
    def __init__(self, api, data):
        super().__init__(api, data)

        if 'groups' not in self._attrs:
            self._attrs['groups'] = []

        if 'triggers' not in self._attrs:
            self._attrs['triggers'] = {}

    def __str__(self):
        return '{}[{}]'.format(self._attrs['name'])

    def add_group(self, group, path, permission):
        assert isinstance(path, Path)

        group_job = {
            'id': group.id,
            'permission': permission.value,
            'path': path.get_object()
        }

        self._attrs['groups'].append(group_job)

    def add_source_group(self, group, path):
        self.add_group(group, path, Permission.SOURCE)

    def add_destination_group(self, group, path):
        self.add_group(group, path, Permission.DESTINATION)

    def save(self):
        if not self.created:
            self._attrs = self._create_job(self._attrs)
        else:
            self._attrs = self._update_job(self.id, self._attrs)

    def fetch(self):
        self._attrs = self._get_job(self.id)

    def _set_sheduler_params(self, start, finish):
        if start is not None:
            self._attrs['scheduler']['start'] = start
        if finish is not None:
            self._attrs['scheduler']['finish'] = finish

    def schedule_now(self, start=None, finish=None):
        self._attrs['scheduler'] = {
            'type': SchedulerType.NOW.value
        }
        self._set_sheduler_params(start, finish)

    def schedule_once(self, time, start=None, finish=None):
        self._attrs['scheduler'] = {
            'type': SchedulerType.ONCE.value,
            'time': time
        }
        self._set_sheduler_params(start, finish)

    def schedule_manually(self, start=None, finish=None):
        self._attrs['scheduler'] = {
            'type': SchedulerType.MANUALLY.value
        }
        self._set_sheduler_params(start, finish)

    def schedule_hourly(self, every, start=None, finish=None):
        self._attrs['scheduler'] = {
            'type': SchedulerType.HOURLY.value,
            'every': every
        }
        self._set_sheduler_params(start, finish)

    def schedule_daily(self, every, time, start=None, finish=None):
        self._attrs['scheduler'] = {
            'type': SchedulerType.DAILY.value,
            'every': every,
            'time': time
        }
        self._set_sheduler_params(start, finish)

    def schedule_weekly(self, days, time, start=None, finish=None):
        self._attrs['scheduler'] = {
            'type': SchedulerType.WEEKLY.value,
            'days': days,
            'time': time
        }
        self._set_sheduler_params(start, finish)

    def add_trigger(self, type, attrs):
        self._attrs['triggers'][type] = attrs

