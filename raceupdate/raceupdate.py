#!/usr/bin/python3

import os
import json
import feedparser

from raceupdate.send_email import send_email
from raceupdate.read_json import output_config
from raceupdate.scrape_torrent import scrape_torrent

url = "https://www.demonoid.pw/rss/users/smcgill1969.xml"
#dir_path = os.path.dirname(os.path.realpath(__file__))
#feedData = dir_path + "/static/config.json"
feedData = os.path.expanduser(os.path.join("~/.config/raceupdate/static/","config.json"))

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

# vars to only find Races that are SD
# I don't need the HD or the Qualifying rounds
race_list = ['SD','Race']
jsonTime = output_config()["time"]

def updateJsonFile(json_key,json_value):
    jsonFile = open(feedData,"r")
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data[json_key]
    data[json_key] = json_value

    jsonFile = open(feedData, "w+")
    jsonFile.write(json.dumps(data,indent=4,sort_keys=True))
    jsonFile.close


def main():
    # does the time match?
    if(jsonTime != entry_published):

        print("Time has changed.  Updating...")
        print(entry_title)
        updateJsonFile("title",entry_title)
        updateJsonFile("time",entry_published)
        updateJsonFile("newUpdate",yesUpdate)
        updateJsonFile("torrent_link",entry_link)

        # right here we need to check if this is just the SD version of the race only!
        if all(x in entry_title for x in race_list):
            print("Match!")
            send_email("New Race", entry_title)
            scrape_torrent()
        else:
            print("No match")

    else:
        updateJsonFile("newUpdate",noUpdate)

if __name__ == "__main__":
    main()
