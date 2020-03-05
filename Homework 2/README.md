# Homework 2


The purpose of this homework is to reverse engineer a 
website's IP addresses.
It is similar to ping assignment, but rather than send out
pings, we will conduct DNS lookups for a single website.
The code should then store the time and IP address into
a comma-separated value (CSV) file. 
A laterPython assignment (H3) will then take that CSV 
and run some basic analysis on this data.

## Helpful Commands
### PowerShell

You will need to look up the DNS mapping of hostnames
and IP addresses.

You can do it using Powershell

```powershell
Resolve-DnsName
```
In PowerShell, you can concatenate strings using
this [Stack Overflow](https://stackoverflow.com/questions/15113413/how-do-i-concatenate-strings-and-variables-in-powershell) answer.

To append to a file, use `Out-File` 

```powershell
Out-File -Append -FilePath [file] -InputObject [data]
```

You can schedule the Powershell Task using
the [Windows Task Scheduler](https://social.technet.microsoft.com/wiki/contents/articles/38580.configure-to-run-a-powershell-script-into-task-scheduler.aspx).

### bash

To perform the lookup with bash:

```bash
nslookup
```



## Storing results
Results should be stored in a CSV file with two columns.
For example, the raw output should look like:

```
timestamp,address
2020-03-05 10:15:00AM,192.168.1.10
2020-03-05 10:30:00AM,192.168.1.10
2020-03-05 10:45:00AM,192.168.1.11
```
The timestamp format you use may be different. It should at least include the date and time.

You may wish to test the CSV file. You 
can attempt to open it with a spreadsheet, like Excel.
When opened in Excel, it should look like:

| timestamp           | address      |
|---------------------|--------------|
| 2020-03-05 10:15:00 | 192.168.1.10 |
| 2020-03-05 10:30:00 | 192.168.1.10 |
| 2020-03-05 10:45:00 | 192.168.1.11 |


Including the header in the file is optional for now,
but worth an extra point. The file without the header would
look like:

```
2020-03-05 10:15:00AM,192.168.1.10
2020-03-05 10:30:00AM,192.168.1.10
2020-03-05 10:45:00AM,192.168.1.11
```

## Submissions

Submit code and screenshots demonstrating the code functionality to the [Github course page](https://classroom.github.com/a/5BJtAPCT).

## Scoring

### 1. Get DNS entries (2 pts)
- Show that the program can separate the IPv4 address
  from other information in the lookup (1 pt)


### 2. Store results in CSV file (4 pts)
- The file should be properly formatted (1 pt)
- The file should contain multiple entries (1 pt)
- The file contains greater than 100 entries (1 pt)
- The file contains a header of: `date,timestamp` (1 pt)

### 3. Run program on regular schedule 
- Demonstrate the ability of the script to run 
  and collect data at regular intervals of 15 minutes (1 pt)
