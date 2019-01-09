# AutoExtend_pythonanywhere
A simple bash+python implementation to be put in a pythonanywhere console and use it's webapp and tasks forever.

```sh
# Usage:
curl -o pyAnywAuto.sh https://raw.githubusercontent.com/smartm13/AutoExtend_pythonanywhere/master/pythonAnywhere_AutoRefresh.sh
bash pyAnywAuto.sh <uname> <passw> [<seconds-interval>=1month] [count=-1] [logtimestamp-timezone=Asia/Kolkata]
```

Update:  
pythonanywhere console dies after some idle time, so it is pointless to trust it for extending purposes.  
You might need to run the script someplace else and leave it running.  
If you cannot host the script for long period of time in your local or some place else,  
You can use pythonanywhere tasks to schedule running the script:  
Goto tasks tab,  
Add a daily task:  
```sh
bash /home/<username>/pyAnywAuto.sh <username> <password> 5 1
#it says extend webapp+task for <username> for 1 times. [in the interval of 5secs-pointless] 
```
This will ensure our script is ran daily, which in turn extends the webapp and task itself.

Note: In case, you already had a task for your own purposes, make a new bash script that does both the tasks, and use that bash script in task tab.
