import requests
from .base_connection import BaseConnection
from .models import Agent, Group, Job


class ConnectApi(BaseConnection):
    def __init__(self, address, token, verify=False):
        super().__init__(address, token, verify)

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

    # Groups
    def create_group(self, name, agents, description=''):
        attrs = {
            'name': name,
            'description': description,
            'agents': [{'id': a.id} for a in agents]
        }

        attrs = self._create_group(attrs)
        return Group(self, attrs)

    def get_groups(self):
        groups_attrs = self._get_groups()
        return [Group(self, attrs) for attrs in groups_attrs]

    def get_group(self, group_id):
        attrs = self._get_group(group_id)
        return Group(self, attrs)

    # Jobs
    def new_job(self, type, name='', description=''):
        attrs = {
            'type': type.value,
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