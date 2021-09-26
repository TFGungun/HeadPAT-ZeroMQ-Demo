#
#   server in Python
#   Binds REP socket to tcp://*:5555
#
#

import time

import zmq

import pattable

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

pattables = pattable.makeDefpattables()

while True:
    #  Wait for next request from client
    name_to_pet = socket.recv_string()
    print("Received request: %s" % name_to_pet)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    if (name_to_pet in pattables):
        socket.send_pyobj(pattables[name_to_pet])
    else:
        socket.send_pyobj(None)
