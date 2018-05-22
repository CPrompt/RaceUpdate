#!/usr/bin/python3

'''
This script is to work on extracting the link from a site.
In particular this site (demonoid) will have a link to the
actual torrent hosted by "hypercache".

This will look for the link in the page to hypercache and return just that.

Next will be to use wget to download that file and then rename it.

Using wget downloads an html page but it is really a torrent file.

'''

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import requests
import re
import wget
import os
import subprocess
import glob
from read_json import *
import shutil

def scrape_torrent():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    rename_file = os.path.join(current_directory,"*.html*")

    try:
        link_request = output_config()["torrent_link"]
        watch_directory = output_config()["watch_directory"]
        entry_title = output_config()["title"]

        page = Request(link_request, headers={'User-Agent': 'Mozilla5/0'})

        webpage = urlopen(page).read()

        soup = BeautifulSoup(webpage,'html.parser')

        print("--------------PROCESSING---------------")

        for a in soup.find_all("a",attrs={"href": re.compile("hypercache")}):
            torrent_file = a['href']
            print("Found URL: ", torrent_file)

            subprocess.run(["wget",torrent_file])

        for filename in glob.glob(rename_file):
            #print(filename)
            new_name = entry_title + ".torrent"
            os.rename(filename,new_name)
            shutil.move(new_name,"/home/curtis/Desktop/")
       
    except:
        print("ERROR!")

if __name__ == "__main__":
    scrape_torrent()

