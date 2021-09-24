#!/usr/bin/env python3

import datetime
import threading
import logging
import random
import time
import pprint

pp = pprint.PrettyPrinter(indent=4)


STREAM_ID = 0
STREAM_ID_TIME = datetime.datetime.utcnow()
print(STREAM_ID_TIME)

MAX_STREAMS = 4
MAX_STREAM_LENGTH = 10
DATA_EXPIRE = 0.5
DATASTREAMS = list()


def main():

    logging.info("Entering")
    print(STREAM_ID_TIME)
    pp.pprint(DATASTREAMS)
    init_datastream()
    pp.pprint(DATASTREAMS)

    dev = MyReader()
    dev.read_stream(2)
    # thread1 = threading.Thread(target=dev.read_stream(), args=(type(dev), 2))
    # thread1.start()
    #
    # thread = list()
    # thread[1] = threading.Thread(target=dev.read_stream, args=(2))
    # thread[1].start()
    # for n in [0, 1]:
    #     thread[n] = threading.Thread(
    #         target=dev.read_stream(),
    #         args=(type(dev), n)
    #     )
    #     thread[n].start()
    logging.info("Exiting")


class MyReader(object):

    def __init__(self):

        self.stream_id = None
        self.message = list()

    def read_stream(self, stream_id):
        global STREAMS

        message = list()
        message_received = False
        while not message_received:
            time.sleep(0.1)
            check_stream_id()
            #print(f"my stream_id {self.stream_id} and {get_stream_id()}")
            if stream_id == get_stream_id():
                data = get_stream_data()
                pp.pprint(get_datastreams())
                if data == 999:
                    message_received = True
                else:
                    message.append(data)
                    get_next_datastream_id()
        print(f"stream_id={stream_id} {message}")


def check_stream_id():
    logging.info("Entering")

    global STREAM_ID
    global STREAM_ID_TIME

    now = datetime.datetime.utcnow()
    data_age = (now - STREAM_ID_TIME).total_seconds()
    logging.debug(f"STREAM_ID = {STREAM_ID}")
    logging.debug(f"data_age = {data_age}")

    if data_age > DATA_EXPIRE:
        get_next_datastream_id()
        STREAM_ID_TIME = datetime.datetime.utcnow()

    logging.info("Exiting")


def get_stream_id():
    logging.info("Entering")
    global STREAM_ID
    logging.info("Exiting")
    return STREAM_ID


def get_datastreams():
    logging.info("Entering")
    global DATASTREAMS
    logging.info("Exiting")
    return DATASTREAMS


def get_next_datastream_id():
    logging.info("Entering")

    global MAX_STREAMS
    global DATASTREAMS
    global STREAM_ID

    success = False
    next_datastream_id = None
    while not success:
        next_datastream_id = random.randint(0, MAX_STREAMS - 1)
        if len(DATASTREAMS[next_datastream_id]) > 0:
            success = True

    STREAM_ID = next_datastream_id
    logging.info("Exiting")


def get_stream_data():
    logging.info("Entering")
    global DATASTREAMS

    data = DATASTREAMS[STREAM_ID].pop()
    logging.info("Exiting")
    return data


def init_datastream():
    logging.info("Entering")

    global DATASTREAMS
    global MAX_STREAM_LENGTH
    global MAX_STREAMS

    logging.debug("Initializing datastreams")
    for stream_num in range(0, MAX_STREAMS):

        stream = [999]  # end of stream
        for stream_elem in range(0, random.randint(1, MAX_STREAM_LENGTH)):
            stream.append(stream_num)

        DATASTREAMS.append(stream)
    logging.info("Exiting")


if __name__ == "__main__":
    FORMAT = '%(asctime)-28s %(levelname)-8s %(funcName)-20s %(message)s'
    logging.basicConfig(
        filename=f"{__name__}.log",
        filemode='a',
        format=FORMAT,
        datefmt='%Y.%m.%d %H:%M:%s',
        level=logging.DEBUG
    )
    main()
    exit()
