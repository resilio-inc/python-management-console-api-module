import requests
from .error import ApiError
from json import JSONDecodeError


BASE_API_URL = '/api/v1'

def api_request(func):
    def wrapper(self, url, *args, **kwargs):
        kwargs['headers'] = {
            'Authorization': 'Token ' + self._token
        }
        kwargs['verify'] = self._verify

        url = self._base_url + '/' + url
        responce = func(self, url, *args, **kwargs)

        try:
            r = responce.json()
        except JSONDecodeError as j:
            r = responce.text

        if 'code' in r and 'message' in r:
            raise ApiError('Error {}: {}'.format(r['code'], r['message']))
        return r
    return wrapper


class BaseConnection:
    def __init__(self, address, token, verify):
        self._token = token
        self._address = address
        self._base_url = address + BASE_API_URL
        self._verify = verify

    # Request methods
    @api_request
    def _get(self, *args, **kwargs):
        return requests.get(*args, **kwargs)

    @api_request
    def _post(self, *args, **kwargs):
        return requests.post(*args, **kwargs)

    @api_request
    def _put(self, *args, **kwargs):
        return requests.put(*args, **kwargs)

    @api_request
    def _delete(self, *args, **kwargs):
        return requests.delete(*args, **kwargs)


    # Agents
    def _get_agents(self):
        return self._get('/agents')

    def _get_agent(self, agent_id):
        return self._get('/agents/%d' % agent_id)

    def _update_agent(self, agent_id, attrs):
        return self._put('/agents/%d' % agent_id, json=attrs)

    def _get_agent_config(self):
        return self._get('/agents/config')


    # Jobs
    def _get_jobs(self):
        return self._get('/jobs')

    def _get_job(self, job_id):
        return self._get('/jobs/%d' % job_id)

    def _create_job(self, attrs):
        return self._post('/jobs', json=attrs)

    def _update_job(self, job_id, attrs):
        return self._put('/jobs/%d' % job_id, json=attrs)


    # Groups
    def _get_groups(self):
        return self._get('/groups')

    def _get_group(self, group_id):
        return self._get('/groups/%d' % group_id)

    def _create_group(self, attrs):
        return self._post('/groups', json=attrs)

    def _update_group(self, group_id, attrs):
        return self._put('/groups/%d' % group_id, json=attrs)
        