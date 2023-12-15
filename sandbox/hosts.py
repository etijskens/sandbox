import re
import sys

def parse_hosts_and_slots(hosts):
    host_names = []
    host_to_slots = {}

    host_list = hosts.split(',')
    pattern = re.compile(r'^[\w.-]+:[0-9]+$')
    for host in host_list:
        if not pattern.match(host.strip()):
            raise ValueError('Invalid host input, please make sure it has '
                             'format as : worker-0:2,worker-1:2.')
        hostname, slots = host.strip().split(':')
        host_names.append(hostname)
        host_to_slots[hostname] = int(slots)
    return host_names, host_to_slots

if __name__=="__main__":
    hosts = sys.argv[1]
    print(f'hosts={hosts}')
    print(parse_hosts_and_slots(hosts))
    print("-*# ok #*-")