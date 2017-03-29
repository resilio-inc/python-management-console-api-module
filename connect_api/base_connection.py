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

        if responce.status_code > 400:
            try:
                r = responce.json()
            except JSONDecodeError:
                r = responce.text
            text = r['message'] if isinstance(r, dict) and 'message' in r else r
            raise ApiError('Error {}: {}'.format(responce.status_code, text))

        return responce
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

    # Helpers
    def _create(self, *args, **kwargs):
        r = self._post(*args, **kwargs)
        return r.headers['Location'] if 'Location' in r.headers else None

    def _get_json(self, *args, **kwargs):
        r = self._get(*args, **kwargs)
        try:
            return r.json()
        except JSONDecodeError:
            raise ApiError('Responce is not a json: ' + r.text)

    # Agents
    def _get_agents(self):
        return self._get_json('/agents')

    def _get_agent(self, agent_id):
        return self._get_json('/agents/%d' % agent_id)

    def _update_agent(self, agent_id, attrs):
        self._put('/agents/%d' % agent_id, json=attrs)

    def _get_agent_config(self):
        return self._get_json('/agents/config')

    def _delete_agent(self, agent_id):
        self._delete('/agents/%d' % agent_id)


    # Jobs
    def _get_jobs(self):
        return self._get_json('/jobs')

    def _get_job(self, job_id):
        return self._get_json('/jobs/%d' % job_id)

    def _create_job(self, attrs):
        location = self._create('/jobs', json=attrs)
        return int(location.split('/')[-1])

    def _update_job(self, job_id, attrs):
        self._put('/jobs/%d' % job_id, json=attrs)

    def _delete_job(self, job_id):
        self._delete('/jobs/%d' % job_id)

    def _get_agent_status(self, job_id, agent_id):
        return self._get_json('/jobs/%d/agents/%d' % (job_id, agent_id))

    def _get_agents_statuses(self, job_id):
        return self._get_json('/jobs/%d/agents' % job_id)


    # Groups
    def _get_groups(self):
        return self._get_json('/groups')

    def _get_group(self, group_id):
        return self._get_json('/groups/%d' % group_id)

    def _create_group(self, attrs):
        location = self._create('/groups', json=attrs)
        return int(location.split('/')[-1])

    def _update_group(self, group_id, attrs):
        self._put('/groups/%d' % group_id, json=attrs)

    def _delete_group(self, group_id):
        self._delete('/groups/%d' % group_id)
        