import time
from pebble import concurrent, ProcessExpired
from concurrent.futures import TimeoutError

@concurrent.process(timeout=2)
def function(foo, bar=0):
    time.sleep(5)
    return foo + bar

future = function(1, bar=2)

try:
    result = future.result()
except TimeoutError as error:
    print("function took longer than %d seconds" % error.args[1])
except ProcessExpired as error:
    print("%s. Exit code: %d" % (error, error.exitcode))
except Exception as error:
    print("function raised %s" % error)
    print(error.traceback)
else:
    print(str(result))