#!/usr/bin/env python3

import datetime
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

    print(STREAM_ID_TIME)
    pp.pprint(DATASTREAMS)
    init_datastream()
    pp.pprint(DATASTREAMS)

    r = MyReader(2)
    r.read_stream()
    print("Mesage")
    print(r.message)

    pass


class MyReader(object):

    def __init__(self, id):

        self.stream_id = id
        self.message = list()

    def read_stream(self):
        global STREAMS

        message_received = False
        while not message_received:
            time.sleep(0.1)
            check_stream_id()
            #print(f"my stream_id {self.stream_id} and {get_stream_id()}")
            if self.stream_id == get_stream_id():
                data = get_stream_data()
                pp.pprint(get_datastreams())
                if data == 999:
                    message_received = True
                else:
                    self.message.append(data)
                    get_next_datastream_id()


def check_stream_id():

    global STREAM_ID
    global STREAM_ID_TIME

    now = datetime.datetime.utcnow()
    data_age = (now - STREAM_ID_TIME).total_seconds()
    print(f"STREAM_ID = {STREAM_ID} data_age = {data_age}")

    if data_age > DATA_EXPIRE:
        get_next_datastream_id()
        STREAM_ID_TIME = datetime.datetime.utcnow()


def get_stream_id():
    global STREAM_ID
    return STREAM_ID


def get_datastreams():
    global DATASTREAMS
    return DATASTREAMS


def get_next_datastream_id():

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


def get_stream_data():
    global DATASTREAMS

    data = DATASTREAMS[STREAM_ID].pop()
    return data


def init_datastream():

    global DATASTREAMS
    global MAX_STREAM_LENGTH
    global MAX_STREAMS

    print("Initializing datastreams")
    for stream_num in range(0, MAX_STREAMS):

        stream = [999]  # end of stream
        for stream_elem in range(0, random.randint(1, MAX_STREAM_LENGTH)):
            stream.append(stream_num)

        DATASTREAMS.append(stream)


if __name__ == "__main__":
    main()
    exit()
