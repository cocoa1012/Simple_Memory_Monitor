# Simple_Memory_Monitor

## What is this?
---
This repository provides two python codes:
- [memory_monitor.py](memory_monitor.py)
    <br> Check computer's memory usage periodically and notify user when memory is almostly run off.
- [kill.py](kill.py)
    <br> After finding the abnormal processes which take a lot of memory, this code can kill all processes with the same program name.
## How to use?
---
- Step 1: Make a sender.list and a receiver.list.
<br>
Apply a new gmail account with some [permission configuration](https://support.google.com/accounts/answer/185833).
<br>
Fill in the sender.list and receiver.list as given sample.
<br>
[sender.list](sender.list) includes sender email account and password.
<br>
[receiver.list](receiver.list) includes number of users and eamil addresses of users.

- Step 2: Run [memory_monitor.py](memory_monitor.py) at background.
<br>
    - There are two parameters to adjust in [memory_monitor.py](memory_monitor.py).
    1. mem_threshold: If free memory below to this value( in MB), the monitor would notify the user.
    2. detect_interval: Period of the detect time( in sec).
<br>
    - There are a lot of ways to run code in background, and you can use your own method.
<br>
For example,
<br>
this command would run the code in background and output the log to mem.log file.

``` console
    nohup python3 -u memory_monitor.py > mem.log &
```

- Step 3: If receiving a mail, check out what happened.
If abnormal detected, you will get mail like:
![mail_screen_shot](/images/mail_screen_shot.jpg "mail_screen_shot")
And then, tou can use tools like [htop](https://github.com/hishamhm/htop) to figure out what happened.
- Step 4: If there is a large number of processes, use [kill.py](kill.py) to kill them all.
<br>
If you found somthing like this:

![htop_screen_shot](/images/htop_screen_shot.png "htop_screen_shot")
Use [kill.py](kill.py) to kill all processes.
``` console
    sudo python3 kill.py <program_name>
```

## About
---
This tool is something like toy comparing to other mature programs. Maybe simple and buggy but easy to use. Any problem may happen when you use it :).