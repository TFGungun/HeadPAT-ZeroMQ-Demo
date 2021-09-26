#
#   client in Python
#   Connects REQ socket to tcp://localhost:5555
#

import random

import zmq

import pattable

context = zmq.Context()

pattable_names = ["Nergigante", "Tiger", "Cat", "Elemental Slime", "Rathalos"]

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

headpats = 0

#  Do 10 requests, waiting each time for a response
for request in range(10):
    pattable_name = random.choice(pattable_names)
    print("Sending number ", request, " to pat ", pattable_name)
    socket.send_string(pattable_name)

    #  Get the reply.
    pattable_object = socket.recv_pyobj()
    if (pattable_object is None):
        print("Oh no, couldn't pat ", pattable_name)
    else:
        patted_part = random.choice(pattable_object.pattable_parts)
        print("Patted ", pattable_object.name,
              "'s ", patted_part, " successfully!")
        if(patted_part == "head"):
            headpats += 1

print("Whoo! We did ", headpats, " headpats!")
