import random
import time

import zmq

import pattable

# Push-Pull is mostly used to make sorts of pipelines and such

pattables = pattable.makeDefpattables()

print(pattables)


def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:5557")
    # MUST start consumer (push_puller) and result collectors (puller) before start producers
    for i in range(20):
        socket.send_pyobj(random.choice(pattables))


producer()
