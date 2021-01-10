import time

from pebble import concurrent
from concurrent.futures import TimeoutError

import gpsd


@concurrent.process(timeout=2)
def conn():
    gpsd.connect()


class Gps:
    f = conn()

    def __init__(self):
        try:
            result = self.f.result()  # blocks until results are ready
            print("tuto benne")
        except TimeoutError as error:
            print("Function took longer than %d seconds" % error.args[1])

    @property
    def status(self):
        try:
            if len(gpsd.state['devices']['devices']) > 0:
                return True
        except KeyError:
            return False
