#!/usr/bin/python

import os
import json
import feedparser

from send_email import send_email
from read_json import *
from scrape_torrent import scrape_torrent

url = "https://www.demonoid.pw/rss/users/smcgill1969.xml"
dir_path = os.path.dirname(os.path.realpath(__file__))
feedData = dir_path + "/config.json"

noUpdate = "No"
yesUpdate = "Yes"

d = feedparser.parse(url)
title = d.feed.title
last_updated = d.feed.updated
feed_id = d.feed.id
updated_parsed = d.feed.updated_parsed

entry_title = d.entries[0].title
entry_published = d.entries[0].updated
entry_link = d.entries[0].link

def updateJsonFile(json_key,json_value):
    jsonFile = open(feedData,"r")
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data[json_key]
    data[json_key] = json_value

    jsonFile = open(feedData, "w+")
    jsonFile.write(json.dumps(data,indent=4,sort_keys=True))
    jsonFile.close

if __name__ == "__main__":
    jsonTime = output_config()["time"]
    print("------------------")
    print(entry_link)
    
    if(jsonTime != entry_published):
        print("Time has changed.  Updating...")
        print(entry_title)
        updateJsonFile("title",entry_title)
        updateJsonFile("time",entry_published)
        updateJsonFile("newUpdate",yesUpdate)
        updateJsonFile("torrent_link",entry_link)
        send_email("New Race",entry_title)
        scrape_torrent()
    else:
        updateJsonFile("newUpdate",noUpdate)
