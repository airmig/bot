import logging
import concurrent.futures
import time
import urllib.request

URL = "http://eai.today"
CHECK_TIME = 3

class TestLog:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(process)d %(name)s %(levelname)s %(message)s")
        logging.info("Log initialized")

def init():
    TestLog()
    logging.info("program initialized")
    return True

def main():
    init()
    logging.info("main started")
    # query url
    while True:
        try:
            urllib.request.urlopen(URL)
        except:
            logging.exception("an exception has occurred")
            logging.info(f"{URL} DOWN")
        # run if try or except did not run any error
        else:
            logging.info(f"{URL} UP")
        time.sleep(CHECK_TIME)
    # catch any exceptions
    # sleep between calls
    logging.info("main end")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as e:
        e.submit(main)
    logging.info("program end")
