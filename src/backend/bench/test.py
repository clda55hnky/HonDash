import threading
from time import sleep

import gpsd


def hanging_function():
    gpsd.connect()

thread = threading.Thread(target=hanging_function)
thread.daemon = True
thread.start()

thread.join(9)
if thread.is_alive():
    print("Function is hanging!")