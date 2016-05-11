import re
from time import time
from utilities.iperf import IPerfClient
from utilities.plink import PLink


class Machine(object):
    def __init__(self, machine_details, timeout=5):
        self._timeout = timeout
        if machine_details:
            self.ip = machine_details.ip
            self.user = machine_details.user
            self.password = machine_details.password
            self.access_point = machine_details.access_point

            self._plink = PLink(self.ip, self.user, self.password)
        self.iperf_result = dict()

    def iperf_server(self):
        pass

    def iperf_client(self, server_ip, print_result=True):
        iperf_client = IPerfClient(server_ip)
        self._plink.command(iperf_client.command())
        self._plink.start()

        pattern = '(\d+\.\d+)\sMbits/sec'
        speed_pattern = re.compile(pattern)
        if print_result:
            iperf_result = list()
            while self._plink.is_alive():
                if len(self._plink.log) > 0:
                    line = self._plink.log.pop()
                    regex_temp = speed_pattern.search(line)
                    if regex_temp:
                        iperf_result.append((time(), float(regex_temp.group(1))))
            self.iperf_result['result'] = iperf_result
            self.iperf_result['average'] = format(sum(v[1] for v in iperf_result)/float(len(iperf_result)), '.2f')
            print('iperf_result {}: {}' .format(self.ip, self.iperf_result))

    def ubuntu_version(self):
        command = 'lsb_release -a'
        self._plink.command(command)
        self._plink.start()

    def user_name(self):
        command = 'whoami'
        self._plink.command(command)
        self._plink.start()


