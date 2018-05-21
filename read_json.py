#!/usr/bin/python
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
feedData = dir_path + "/config.json"


def read_json(myFeed):
    try:
        json_data = open(myFeed)
        data = json.load(json_data)
    except:
        print("Can't open")
    return data

def use_list(passed_list):
    return passed_list

def output_config():
    returned_list = read_json(feedData)
    config_dict = use_list(returned_list)
    return config_dict

if __name__ == "__main__":
    test = output_config()["title"]
    print(test)
