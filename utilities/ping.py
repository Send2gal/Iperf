import os


class Ping(object):
    @staticmethod
    def test(ip, n=1, l=32):
        if os.system("ping {} -n {} -l {}".format(ip, n, l)) == 0:
            return True
        else:
            return False

