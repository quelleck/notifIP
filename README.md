# notifIP
Script that triggers an IFTTT recipe when your public IP address changes.

Just add your IFTTT API key and recipe in config/ip_checker.conf.

The script uses ipinfo.io which has a limit of 1000 requests per day for free. If you set up a cron job, be sure to run it no faster than once every two minutes to not get rate limited.
