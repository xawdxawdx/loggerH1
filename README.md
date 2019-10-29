# LoggerH1
Python script for logging changes in hacker's reputation on h1. Currently nice work with mailru (hardcoded)

## How to use ?

Execute python3 input.py and enter your program name. For example if https://hackerone.com/mailru -> mailru .

Provide a correct pathes for log files, such as `/var/www/html/loggerH1/` and directories for json files `/root/tools/loggerH1/programs/`

Create a cron with this expression `*/1 * * * * /usr/local/bin/python3 /root/tools/loggerH1/logger.py > /tmp/test.log 2>&1 `

There will be program's log file on /var/www/html/loggerH1/mailru_log.txt

You can use this script as a bot for social network VK - he can send you a messages about triages and e.t.c to your account

## Nowadays

Now this script just checks:
```diff
! triages
+ (+2 rep)
- Non Applicable
Need more info
```
UPD: 
$$$
Low, Medium and High bounties was added !
$$$
