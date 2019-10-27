# loggerH1
Python script for logging changes in hacker's reputation on h1

# How to use ?

Put your bugbounty program name in json request like this `team(handle:\"mailru\")`

Provide a correct pathes for log files, such as `/var/www/html/mrglog.txt` and json files `/root/tools/loggerH1/mrg.json`

Create a cron with this expression `*/1 * * * * /usr/local/bin/python3 /root/tools/loggerH1/test.py > /tmp/test.log$`

# Nowadays

Now this script just checks `triages`, `duplicates`(+2 rep), `N/A` and `need more info`
