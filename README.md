# RaceUpdate

Real simple python script that looks at the RSS feed for SMcGill1969
and will send a text message if there is an update

This will then go to the link in the feed and parse out where the torrent file is located.
Demonoid does not place a direct link to the torrent file in the RSS feed

Once it goes to that page, BeautifulSoup will scan through to get the link to save the file.  Then I use wget to download the file.

However...this file is downloaded with an HTML extension (i.e. index.hmtl?uid=0 or something)
Once that is downloaded, it will then rename the file to the race name with the extension .torrent

Only thing left is to move it to the watch folder for rtorrent to pick up

Setup:

	Required:
		Python3
	
	Libs:
		wget
		feedparser
		BeautifulSoup

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
Then you will need to add the __init__.py file to 

Then I have a cron set to run every 1/2 hour only on Sundays because...that's Race Day!

For the cron to send a text message, I had to create a bash script that simply called the "send_email.py" file

