import sys
import datetime
import time
import requests
import json

URL = "http://ir.eia.gov/ngs/wngsr.json"

def convert_time_now():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    return datetime.datetime.strptime(time, "%H:%M:%S").time()

def get_data():
    net_change_list = []
    response = requests.get(URL)
    convert_json = json.loads(response.text[3:])
    print("Total net change :{}".format(convert_json["series"][0]["calculated"]["net_change"]))
    for i in range(1, len(convert_json["series"])):
        net_change_list.append(convert_json["series"][i]["calculated"]["net_change"])
    print("Average net change :{}".format(sum(net_change_list) / len(net_change_list)))

now = convert_time_now()
start_time = datetime.time(int(sys.argv[1]), int(sys.argv[2]))
if start_time > now:
     sleep_sec = (((start_time.hour - now.hour) * 60) + (start_time.minute - now.minute)) * 60
elif start_time <= now:
     sleep_sec = (86400 - (((now.hour * 60) + now.minute) * 60)) + ((start_time.hour * 60) + (start_time.minute) * 60)
time.sleep(sleep_sec)

get_data()