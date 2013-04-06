from bs4 import BeautifulSoup
import sys
import subprocess


i=1
i=int(sys.argv[1])
stop=int(sys.argv[2])
print(i)

while (i<stop):
   retcode = subprocess.call(["wget", "--tries=100", "--retry-connrefused", "http://games.crossfit.com/athlete/"+str(i)])
   print(i)
   i=i+1





