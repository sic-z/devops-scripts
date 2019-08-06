import requests


class MesosAPI:
    def __init__(self, ip, port=5050, auth_token=''):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s' % (ip, port)
        self.headers = {'authorization': 'Basic %s' % auth_token}

    def get(self, path, timeout=20.0):
        try:
            response = requests.get(self.url + path,
                                    headers=self.headers,
                                    timeout=timeout)
            return response
        except requests.exceptions.RequestException:
            print 'Get %s failed' % path
            return None

    def get_leader(self):
        state = self.get_state()
        return state.json()['leader']

    def get_state(self, timeout=20.0):
        return self.get('/state.json', timeout=timeout)

    def get_state_summary(self, timeout=20.0):
        return self.get('/state-summary', timeout=timeout)

    def get_version(self):
        return self.get('/version')
    
    def get_metrics_snapshot(self):
        return self.get('/metrics/snapshot')

    def get_frameworks(self):
        return self.get('/frameworks')

    def get_tasks(self):
        return self.get('/tasks')



