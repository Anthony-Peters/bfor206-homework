# Homework 1


The purpose of this homework is to develop a bash script that uses the ping 
command to test whether a device is online. The results of this script 
should be logged with a timestamp. The script should be run as a cron job. 
If a server is not responding, email the system administrator (you).

## Useful commands
### ping
```console
ping 192.168.1.1 -c3
ping google.com -c3
```
### cut
Split a string using the percentage sign and 
get the first part of the split:

```console
echo “100% awesome” | cut -d”%” -f1
```
Get the second split:

```console
echo “100% awesome” | cut -d”%” -f2
```

Split using space instead of percentage:

```console
echo “100% awesome” | cut -d” ” -f1
```

### mail (from mailutils package)

- Set up a local account (you will see the prompts when installing)

```console
# to send a message using echo
echo “message body” | mail -s “subject” lee@lee.local

# check mail with:
cat /var/mail/lee
```

## Script functionality

- Create a function that accepts an IP address or hostname as an argument
- Parse the output of the ping command
- Check the output status
- If the ping is not responding or is missing packets, report this to the log 
and send an email
- If the ping is high latency, report this to the log and send an email
- If the device is normal, report this to the log
- The script should run every five minutes.


## Scoring

### 1. Ping devices (3 pts)
- Show that the script pings addresses
- You should ping at least 3 addresses. One of the addresses 
- should contain your UAlbany NetID. For 
example, a NetID of AB123456 should ping 12.34.56.1.

### 2. Log information (2 pts)
- Show the log file with script output. The logs should have a 
timestamp for each entry

### 3. Email when getting errors (3 pts)
- Show the emails you receive from the failed pings for the out of service IP address 

### 4. Run task at regular intervals (3 pts)
- Show crontab and the log file with regular intervals

##Submission
Submit code and screenshots demonstrating the code functionality to the [Github course page](https://classroom.github.com/a/5BJtAPCT).




