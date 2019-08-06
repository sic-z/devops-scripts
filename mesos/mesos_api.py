import requests
import json

API_URL = '/api/json'
QUEUE_API_URL = '/queue' + API_URL
OVERALL_LOAD_API_URL = '/overallLoad' + API_URL
COMPUTER_API_URL = '/computer' + API_URL


def concatenate_api_url(api_path):
    if api_path.startswith('/'):
        return api_path + API_URL
    else:
        return '/' + api_path + API_URL


class Jenkins:
    def __init__(self, url, user, passwd):
        """

        :type url: str
        :type user: str
        :type passwd: str
        """
        self._url = url
        self._user = user
        self._passwd = passwd

    def get(self, url, params=None, timeout=10):
        try:
            response = requests.get(url, params, auth=(self._user, self._passwd),
                                    timeout=timeout)
            response_json = json.loads(response.text)
            return response_json
        except Exception:
            raise

    def post(self, url, params=None, timeout=10):
        try:
            response = requests.post(url, params, auth=(self._user, self._passwd),
                                     timeout=timeout)
            print response.status_code
            response_json = json.loads(response.text)
            return response_json
        except Exception:
            raise

    def get_info(self):
        pass

    def get_queue(self, params=None, timeout=10):
        queue_json = self.get(self._url + QUEUE_API_URL, params, timeout)
        return queue_json['items']

    def queueing_jobs_count(self):
        queue = self.get_queue()
        return len(queue)

    def is_queueing(self):
        return self.queueing_jobs_count() != 0

    def get_running_builds(self, timeout=10):
        params = {
            'tree': 'computer[displayName,executors[currentExecutable[url]],oneOffExecutors[currentExecutable[url]]]',
            'xpath': '//url',
            'wrapper': 'builds'
        }
        return self.get(self._url + COMPUTER_API_URL, params, timeout)

    def get_running_builds_list(self):
        running_builds = self.get_running_builds()
        running_builds_list = []

        for computer in running_builds['computer']:

            for executor in computer['executors']:
                if executor['currentExecutable'] is not None:
                    running_build_url = executor['currentExecutable']['url']
                    running_builds_list.append(running_build_url)

            for executor in computer['oneOffExecutors']:
                if executor['currentExecutable'] is not None:
                    running_build_url = executor['currentExecutable']['url']
                    running_builds_list.append(running_build_url)

        return running_builds_list

    def is_job_running(self):
        return len(self.get_running_builds_list()) != 0

    def get_jobs(self, params=None, timeout=10):
        api_json = self.get(self._url + API_URL, params, timeout)
        jobs = api_json['jobs']
        return jobs

    def get_jobs_name_list(self):
        jobs_name_list = []
        jobs = self.get_jobs()
        for job in jobs:
            jobs_name_list.append(job['name'])
        return jobs_name_list

    def get_views(self, params=None, timeout=10):
        api_json = self.get(self._url + API_URL, params, timeout)
        views = api_json['views']
        return views

    def get_computers(self, params=None, timeout=10):
        computer_json = self.get(self._url + COMPUTER_API_URL, params, timeout)
        return computer_json

    def get_job_conf_xml(self, name):
        pass

    def restart(self):
        pass

    def safe_restart(self):
        pass

    def shutdown(self):
        pass

    def safe_shutdown(self):
        pass
