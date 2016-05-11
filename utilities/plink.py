import shlex
import subprocess
import threading

PLINK = r'plink.exe'


class PLink(threading.Thread):

    def __init__(self, ip_host, user, password):
        super().__init__()
        self._ip_host = ip_host
        self._user = user
        self._password = password
        self._command = None
        self.log = list()

    def command(self, _command):
        self._command = _command

    def run(self):
        client = "{}@{} -pw {}".format(self._user, self._ip_host, self._password)
        command = shlex.split("%s %s %s" % (PLINK, client, self._command))

        process = subprocess.Popen(command,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=False)

        while True:
            output = process.stdout.readline().decode("utf-8")
            if output == '' and process.poll() is not None:
                break
            if output:
                # print(output.strip())
                self.log.append(output)

