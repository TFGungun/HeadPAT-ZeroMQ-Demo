import json
import random
import sys
import time

import zmq

import gachasClass as gc

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5555")

gacha_types = ["ten rolls", "single roll"]

limit = 15
attempt = 1
attempt_received = 0

while attempt_received < attempt - 1 or attempt <= limit:

    if (attempt < limit):
        for j in range(random.randint(1, 3)):
            gacha_type = random.choice(gacha_types)
            print("Attempting to do a gacha of " +
                  gacha_type + " type ; attempt #", attempt)
            socket.send_json(json.dumps("client gacha attempt #" + str(
                attempt) + " : " + gacha_type))
            attempt += 1
        print("\n---")
    msg = socket.recv_json()
    msg_obj = json.loads(msg)
    print("Gacha result for attempt ", msg_obj[-1], " :")
    for gacha_res_idx in range(len(msg_obj)-1):
        print(msg_obj[gacha_res_idx])
    attempt_received += 1
    print('---\n')

    time.sleep(1)
