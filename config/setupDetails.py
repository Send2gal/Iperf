from yaml import load
from config.machineDetails import MachineDetails
import os

CONFIG_FILE = os.path.join('config', 'setup.yaml')


class Setup(object):
    def __init__(self, name):
        self._name = name
        self._machines_list = self.load_machines()
        self._access_point, self._machine = self.split_to_access_point_station(self._machines_list)

    def load_machines(self):
        machines = []
        with open(CONFIG_FILE, 'r') as f:
            machines_collection = load(f)
        for machine in (machines_collection[self._name]['machines']):
            machine_name = machines_collection[self._name]['machines'][machine]
            machines.append(MachineDetails(machine_name))
        return machines

    @staticmethod
    def split_to_access_point_station(machines):
        access_point = []
        station = []

        for machine in machines:
            if machine.access_point:
                access_point.append(machine)
            else:
                station.append(machine)

        return sorted(access_point, key=lambda m: m.ip),  sorted(station, key=lambda m: m.ip)

    def machines(self):
        _machines = dict()
        _machines['access_point'] = self._access_point
        _machines['machine'] = self._machine
        return _machines

    def machine(self):
        return self._machine

    def access_point(self):
        return self._access_point
