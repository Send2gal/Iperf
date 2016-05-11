from utilities.plink import PLink


class IPerf(object):

    def __init__(self, interval=1, u=None, format='m'):
        self._interval = interval
        self._u = u
        self._format = format


class IPerfServer(IPerf):

    def __init__(self):
        super().__init__()


class IPerfClient(IPerf):

    def __init__(self, server_ip, parallel=None, timeout=10):
        super().__init__(interval=1, u=None, format='m')
        self._server_ip = server_ip
        self._parallel = parallel
        self._timeout = timeout

    def command(self):
        return "iperf -c{} -i{} -t {} -f {}".format(self._server_ip, self._interval, self._timeout, self._format)






