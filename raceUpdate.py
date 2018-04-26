#!/usr/bin/python

import json
import feedparser
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromEmail = "cprompt@triad.rr.com"
toEmail = "3363379174@vtext.com"
emailLogin = "cprompt@triad.rr.com"
emailPass = "Philter69"
emailServer = "mail.twc.com"
emailPort = "587"

url = "https://www.demonoid.pw/rss/users/smcgill1969.xml"

d = feedparser.parse(url)
title = d.feed.title
last_updated = d.feed.updated
feed_id = d.feed.id
updated_parsed = d.feed.updated_parsed

entry_title = d.entries[0].title
entry_published = d.entries[0].updated

feedData = "/home/curtis/Scripts/RaceUpdate/config.json"

#print(title)
#print(entry_title)
#print(entry_published)

def send_email(emailSubject,emailBody):
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = emailSubject

    body = emailBody

    msg.attach(MIMEText(body,'plain'))

    s = smtplib.SMTP(emailServer,emailPort)
    s.ehlo()
    s.starttls()
    s.login(emailLogin,emailPass)
    text = msg.as_string()
    s.sendmail(fromEmail,toEmail,text)
    s.quit()

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


def updateJsonFile(json_key,json_value):
    jsonFile = open(feedData,"r")
    data = json.load(jsonFile)
    jsonFile.close()

    tmp = data[json_key]
    data[json_key] = json_value

    jsonFile = open(feedData, "w+")
    jsonFile.write(json.dumps(data,indent=4,sort_keys=True))
    jsonFile.close

#updateJsonFile("time","NEWER!")
#updateJsonFile("path","/home/new_path/")

if __name__ == "__main__":
    jsonTime = output_config()["time"]

    if(jsonTime != entry_published):
        print("Time has changed.  Updating...")
        updateJsonFile("title",entry_title)
        updateJsonFile("time",entry_published)
        send_email("New upload",entry_title)
    else:
        updateJsonFile("time",entry_published)

    #print(output_config()["time"])
