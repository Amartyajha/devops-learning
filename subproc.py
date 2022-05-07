from curses.ascii import SUB
from re import T, sub
import subprocess
from tabnanny import check
from turtle import pen
#subprocess.run('ls -laH', shell=True)
# OR 
data=subprocess.run(['ls', '-llstrh'], capture_output=True,text=True, check=True)
print(data.stdout)
