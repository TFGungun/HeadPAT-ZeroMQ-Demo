#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
#
import pickle
import time
from random import randrange

import zmq

import gachaClass as gc

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

gachasBanners = gc.defBannersMaker()

day = 0
gacha_index = 0

while True:
    print("day ", day)
    # socket.send_pyobj(gachasBanners[gacha_index])
    socket.send_multipart([(gachasBanners[gacha_index].name).encode(),
                          bytes(day.to_bytes(day.bit_length(), byteorder="big")), pickle.dumps(gachasBanners[gacha_index])])

    day += 1
    gacha_index += 1
    if(gacha_index >= len(gachasBanners)):
        gacha_index = 0

    time.sleep(3)
