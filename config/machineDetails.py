import yaml
import os

CONFIG_FILE = os.path.join('config', 'machines.yaml')


class MachineDetails(object):
    def __init__(self, station_name):
        with open(CONFIG_FILE, 'r') as config:
            station = yaml.load(config)

        self.ip = station[station_name]['ip']
        self.user = station[station_name]['user']
        self.password = station[station_name]['password']
        self.access_point = station[station_name]['accessPoint']

    def __str__(self):
        return(self.ip)
