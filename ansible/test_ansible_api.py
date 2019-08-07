from ansible_api import AnsibleAPI

a = AnsibleAPI("dchosts")
host_list = ['node1']
tasks_list = [
    dict(action=dict(module='command', args='hostname')),
    dict(action=dict(module='shell', args='python sleep.py')),
    dict(action=dict(module='synchronize', args='src=/home/op/test dest=/home/op/ delete=yes')),
]
result = a.run_ansible(host_list,tasks_list)
print result
playbook_result = a.run_playbook(playbook_path=['test.yml'])
print playbook_result
