import multiprocessing
import threading

import gpsd

CONNECT_TIMEOUT = 5


class Gps:
    def __init__(self):
        self.packet = None

        self._connect()
        if self.status:
            threading.Thread(target=self._update).start()
        else:
            print("no conecta")

    @staticmethod
    def gpsde():
        gpsd.connect()

    def _connect(self):
        process = multiprocessing.Process(target=gpsd.connect())
        process.daemon = True
        process.start()
        process.join(CONNECT_TIMEOUT)

        if process.is_alive():
            print("Function is hanging!")

    @property
    def status(self):
        try:
            if len(gpsd.state['devices']['devices']) > 0:
                return True
        except KeyError:
            return False

    @property
    def speed(self):
        try:
            return self.packet.speed()
        except (AttributeError, gpsd.NoFixError):
            return -1

    def _update(self):
        try:
            while self.status:
                self.packet = gpsd.get_current()
        except UserWarning:
            pass
            #self.__init__()
