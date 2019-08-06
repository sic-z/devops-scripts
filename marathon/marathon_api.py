# -*- coding:utf-8 -*-

import requests

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'}


def set_headers(auth_token):
    headers = HEADERS.copy()
    if auth_token and auth_token != '':
        headers['Authorization'] = 'basic ' + auth_token
    return headers


class Marathon:
    def __init__(self, ip, port=8080, auth_token=''):
        """

        :type auth_token: string
        """
        self.ip = ip
        self.port = port
        self.auth_token = auth_token
        self.headers = set_headers(auth_token)

    def get(self, path):
        try:
            resp = requests.get('http://%s:%s%s' % (self.ip, self.port, path), headers=self.headers)
            return resp
        except requests.exceptions.RequestException:
            print 'Get %s failed!' % path
            return None

    def get_info(self):
        return self.get('/v2/info')

    def get_version(self):
        marathon_info = self.get_info()
        return marathon_info.json()['version']

    def get_leader(self):
        return self.get('/v2/leader').json()

    def get_tasks(self):
        return self.get('/v2/tasks').json()

    def get_deployments(self):
        return self.get('/v2/deployments').json()

    def get_metrics(self):
        return self.get('/metrics').json()

    def get_service_info(self, service_name):
        return self.get("/v2/apps/%s" % service_name).json()

    def get_services_from_tasks(self):
        data = self.get_tasks()
        result = []
        for info in data['tasks']:
            service = info['appId'].replace("/", '')
            result.append(service)
        return result

    def get_service_and_host(self):
        data = self.get_tasks()
        result = {}
        for info in data['tasks']:
            service_name = info['appId'].replace("/", '')
            result[service_name] = info['host']
        return result

    def deploy(self, parameters):
        try:
            response = requests.post('http://%s:%s/v2/apps' % (self.ip, self.port),
                                     headers=self.headers, json=parameters)
            return response
        except requests.exceptions.RequestException:
            print 'Deploy app failed!'
            return None

    def restart(self, app_id, timeout=20.0):
        try:
            response = requests.post('http://%s:%s/v2/apps/%s/restart' % (self.ip, self.port, app_id),
                                     headers=self.headers,
                                     timeout=timeout)
            return response
        except requests.exceptions.RequestException:
            print 'Restart app %s failed!' % app_id
            return None

    def scale(self, app_id, instances, timeout=20.0):
        try:
            response = requests.put('http://%s:%s/v2/apps/%s' % (self.ip, self.port, app_id),
                                    data='{"instances": %s}' % instances,
                                    headers=self.headers,
                                    timeout=timeout)
            return response
        except requests.exceptions.RequestException:
            print 'Scale app %s failed!' % app_id
            return None

    def destroy(self, app_id):
        try:
            response = requests.requests('DELETE', 'http://%s:%s/v2/apps/%s' % (self.ip, self.port, app_id),
                                         headers=self.headers)
            return response
        except requests.exceptions.RequestException:
            print 'Destroy app %s failed!' % app_id
            return None


