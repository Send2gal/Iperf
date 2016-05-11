#!/python35
# -*- coding: utf-8-*-

from config.setupDetails import Setup
from helpers.machine import Machine
from utilities.ping import Ping

machine = []
access_point = []
setup_details = Setup('setup-1').machines()
for m in setup_details['machine']:
    machine.append(Machine(m))

for ap in setup_details['access_point']:
    access_point.append(Machine(ap))


for station in machine:
    Ping.test(station.ip)  # error = "FATAL ERROR: Network error: Connection refused"

for station in machine:
    station.iperf_client('10.0.0.1')

# print("aa")
# for i in range(20):
#     print('-'*100 + '\n', p_link.log + '-'*100)
#     print('is_alive :', p_link.is_alive())
#     sleep(1)