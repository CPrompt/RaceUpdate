# RaceUpdate

## Script has been replaced by "check_races" found here: https://github.com/CPrompt/check_races

This started off as a real simple python script that looks at the RSS feed for SMcGill1969
and send a text message if there is an update.  Since then, I have added  a lot of components.

### Process:
What I was going for was an automated way to check if there was a new torrent.
If so, send a text message and then go ahead and grab the needed torrent.
Once the torrent has been downloaded, move it to the watch folder for rtorrent to pickup and start the download.
After that, rtorrent will take care of moving to the correct directory and sending a text message as notification
that the race is ready to watch!

### More in depth:
We are monitoring the RSS feed coming off of Demonoid using the python package, feedparser.
This will look at the feed and find the needed information, which is mainly,date, title and link which is stored in the json file, "config.json".
Once we have this information, we use urllib2 to read the page from the "link" field and pass that to a variable for BeautifulSoup4.
BeautifulSoup4 then reads all the data and looks for the "a href" tag with the information "hypercache".
That link will download the needed torrent file. However...this file is downloaded with an HTML extension (i.e. index.hmtl?uid=0 or something)
Once that is downloaded, it will then rename the file to the race name with the extension .torrent (i.e. MotoGP 2018x05 France Race BTSportHD SD.torrent)

Now we need move it to the watch folder for rtorrent to pick up.

Required:
	Python3

	Python3 Modules:
		requests
		feedparser
		BeautifulSoup

### A bit of manual configs:
First you will need to create a python file called simply "creds.py" and place in the "loginfo" directory.
I'm not uploading mine!
This is a simple python dictionary in this format:

```python
login = {
        "fromEmail": "<YOUR EMAIL>",
        "toEmail": "<THE PHONE NUMBER TO SEND THE TEXT>",
        "emailLogin": "<SMTP LOGIN USER>",
        "emailPass": "<SMTP LOGIN PASSWORD>",
        "emailServer": "<SMTP SERVER>",
        "emailPort": "<SMTP SERVER PORT>"
        }
```

Leave everything else the same.

Then I have a cron set to run every 1/2 hour only on Sundays because...that's Race Day!
(i.e. ``*/30 * * * 0 python3 /path/to/scrtip/raceUpdate.py``)

For rtorrent to send a text message once complete, I had to create a bash script that simply called the "send_email.py" file.
I added this to my rtorrent file process and is outside of this script

