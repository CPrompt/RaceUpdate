# RaceUpdate

Real simple python script that looks at the RSS feed for SMcGill1969
and will send a text message if there is an update

Setup:

First you will need to create a python file called simply "creds.py" and place in the "loginfo" directory.
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

Then I have a cron set to run every 1/2 hour only on Sundays
