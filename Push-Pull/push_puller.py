import random
import time

import zmq

import pattable


def consumer():
    id_ = random.randrange(1, 10005)
    print("This is consumer #", id_)
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")

    while True:
        pattable = consumer_receiver.recv_pyobj()
        patted_part = random.choice(pattable.pattable_parts)
        patted_head = False
        if (patted_part == "head"):
            patted_head = True

        consumer_sender.send_json(
            {'id': id_, 'pattable': pattable.name, 'patted_part': patted_part, 'headpat': patted_head})


consumer()
