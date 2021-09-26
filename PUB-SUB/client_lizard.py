#
#   client
#   Connects SUB socket to tcp://localhost:5556
#

import pickle
import sys
import time

import zmq

import gachaClass

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

banner_name = "The Lizards of Insanity Banner"

print("Getting " + banner_name +
      " gacha banner drop rates... if available on this day...")
socket.connect("tcp://localhost:5556")

# Subscribe to zipcode, default is NYC, 10001

socket.setsockopt_string(zmq.SUBSCRIBE, banner_name)

# Process 5 updates
while True:
    [topic, day, banner] = socket.recv_multipart()

    banner = pickle.loads(banner)
    print("Today is day ", int.from_bytes(day, 'big'), " and ",
          banner_name, " gacha banner is available!")
    print("Here are the drop rates:")
    banner.printBanner()
    print()
    time.sleep(1.5)
