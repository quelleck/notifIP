# notifIP
Script that triggers an IFTTT recipe when your public IP address changes.

The script uses ipinfo.io which has a limit of 1000 requests per day for free. If you set up a cron job, be sure to run it no faster than once every two minutes to avoid getting rate limited.

#Installation:
Remove .template extention from files in config/

Add your IFTTT API key and recipe name to notifip.conf
