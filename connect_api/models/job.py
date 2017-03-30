from .base_model import BaseModel
from ..constants import Permission, SchedulerType, JobType
from ..utils import Path
from ..error import ApiError


class Job(BaseModel):
    def __init__(self, api, data):
        super().__init__(api, data)

        if 'groups' not in self._attrs:
            self._attrs['groups'] = []

    @property
    def type(self):
        return JobType(self._attrs['type'])

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
            job_id = self._create_job(self._attrs)
            self._attrs['id'] = job_id
        else:
            self._update_job(self.id, self._attrs)
        self.fetch()

    def fetch(self):
        self._attrs = self._get_job(self.id)

    # Scheduler
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

    # Triggers
    def add_trigger(self, name, attrs):
        assert self.type in [JobType.CONSOLIDATION, JobType.DISTRIBUTION], 'Job doesn\'t supports triggers'
        assert name in ['pre_indexing', 'post_download', 'complete'], 'Invalid trigger name'

        if 'triggers' not in self._attrs:
            self._attrs['triggers'] = {}
        self._attrs['triggers'][name] = attrs

    def set_script(self, script):
        assert self.type == JobType.SCRIPT, 'Only script job supports script'

        self._attrs['script'] = script

    # Agent status
    def get_agents_statuses(self):
        return self._get_agents_statuses(self.id)

    def get_agent_status(self, agent_id):
        return self._get_agent_status(self.id, agent_id)

