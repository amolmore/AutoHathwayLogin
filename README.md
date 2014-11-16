# Auto Hathway Login 

This is a small script that will log you in automatically if Hathway logs you out. Hathway kicks you out every few hours and this is very annoying while downloading huge files. This script requires Python 2.7

Usage:
First change the user id and password in the script then run the following code in bash shell.

```
python AutoHathwayLogin.py

```

or to make it run in background use following command . The script will keep runing even if you log off. 
```
nohup python AutoHathwayLogin.py &
```
 sleepTime is in seconds

Changed line 56 to use sh.ping instead of socket
