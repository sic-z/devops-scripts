import marathon_api

ip = '10.XX.XX.XX'
service_name = 'XXX'
marathon = marathon_api.Marathon(ip)
print marathon.get_leader()
print marathon.get_tasks()
print marathon.get_service_and_host()
print marathon.get_service_info(service_name)
