import requests
from .base_connection import BaseConnection
from .models import Agent, Group, Job


class ConnectApi(BaseConnection):
    def __init__(self, address, token, verify=False):
        super(ConnectApi, self).__init__(address, token, verify)

        if not verify:
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Agents
    def get_agents(self):
        agents_attrs = self._get_agents()
        return [Agent(self, attrs) for attrs in agents_attrs]
        
    def get_agent(self, agent_id):
        attrs = self._get_agent(agent_id)
        return Agent(self, attrs)

    def disconnect_agent(self, agent):
        self._delete_agent(agent.id)

    # Groups
    def create_group(self, name, agents, description=''):
        attrs = {
            'name': name,
            'description': description,
            'agents': [{'id': a.id} for a in agents]
        }
        group_id = self._create_group(attrs)

        group = Group(self, dict(id=group_id))
        group.fetch()
        return group

    def get_groups(self):
        groups_attrs = self._get_groups()
        return [Group(self, attrs) for attrs in groups_attrs]

    def get_group(self, group_id):
        attrs = self._get_group(group_id)
        return Group(self, attrs)

    def delete_group(self, group):
        group_id = group.id if isinstance(group, Group) else group
        self._delete_group(group_id)

    # Jobs
    def new_job(self, job_type, name='', description=''):
        attrs = {
            'type': job_type,
            'name': name,
            'description': description
        }

        return Job(self, attrs)

    def get_jobs(self):
        jobs_attrs = self._get_jobs()
        return [Job(self, attrs) for attrs in jobs_attrs]

    def get_job(self, job_id):
        attrs = self._get_job(job_id)
        return Job(self, attrs)

    def delete_job(self, job):
        self._delete_job(job.id)

    def test_connection(self):
        self._get_jobs()