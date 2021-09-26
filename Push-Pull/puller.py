import pprint
import time

import zmq


def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    collecter_data = {}
    head_pats = 0
    for i in range(20):
        result = results_receiver.recv_json()
        print(result)
        if result["headpat"]:
            head_pats += 1

        if result["id"] not in collecter_data:
            collecter_data[result["id"]] = {"id": result["id"], "pats": []}

        collecter_data[result["id"]]["pats"].append(
            {"patted": result["pattable"], "part": result["patted_part"]})
        # collecter_data["id"]["pats"].append(
        #     {"patted": result["pattable"], "part": result["patted_part"]})
        # else:
        #     collecter_data["id"]["pats"] = [
        #         {"patted": result["pattable"], "part": result["patted_part"]}]

    pprint.pprint(collecter_data)


result_collector()
