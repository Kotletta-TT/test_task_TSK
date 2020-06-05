import sys
import datetime
import time
import requests
import json

# RUN WITH TWO ARGUMENTS >python3 test2.py 22 11
URL = "http://ir.eia.gov/ngs/wngsr.json"
SEC = 60
DAY = 24 * 60 * SEC

def convert_time_now():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    return datetime.datetime.strptime(time, "%H:%M:%S").time()

def get_json():
    response = requests.get(URL)
    return json.loads(response.text[3:])

def show_data():
    net_change_list = []
    received_json = get_json()
    print("Total net change :{}".format(received_json["series"][0]["calculated"]["net_change"]))
    for i in range(1, len(received_json["series"])):
        net_change_list.append(received_json["series"][i]["calculated"]["net_change"])
    print("Average net change :{}".format(sum(net_change_list) / len(net_change_list)))


def schedule():
    now = convert_time_now()
    # IF NOT ARGS, TIME WAIT INSTALL TO DEFAULT = 5 SEC
    try:
        start_time = datetime.time(int(sys.argv[1]), int(sys.argv[2]))
        if start_time > now:
            sleep_sec = (((start_time.hour - now.hour) * SEC) + (start_time.minute - now.minute)) * SEC
        elif start_time <= now:
            sleep_sec = (DAY - (((now.hour * SEC) + now.minute) * SEC)) + ((start_time.hour * SEC) + (start_time.minute) * SEC)
        time.sleep(sleep_sec)
    except IndexError:
        time.sleep(5)


def run():
    schedule()
    show_data()

run()