import json
import random
import re
import time

import zmq

import gachasClass as gc

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555")

gachas = gc.defMaker()
pattern = re.compile(r'#\d+')


def gacha_rolls(num):
    gacha_results = []
    for i in range(num):
        gacha_results.append(random.choice(gachas).print())
    return gacha_results


while True:

    msg = socket.recv_json()
    msg_obj = json.loads(msg)
    print("Replying to...", msg_obj)
    gacha_amount = 1
    if ("ten rolls" in msg_obj):
        gacha_amount = 10

    gacha_attempt_num = pattern.findall(msg)
    # print(gacha_attempt_num)
    gacha_results = gacha_rolls(gacha_amount)
    gacha_results.append(gacha_attempt_num[0])

    # print(gacha_results)

    socket.send_json(json.dumps(gacha_results))
    time.sleep(1)
