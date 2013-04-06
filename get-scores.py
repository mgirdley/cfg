#from bs4 import BeautifulSoup
import sys
import subprocess

i=1
division=int(sys.argv[1])
i=int(sys.argv[2])
stop=int(sys.argv[3])
print(i)


while (i<stop):
   #retcode = subprocess.call(["wget", "--tries=100", "--retry-connrefused", "http://games.crossfit.com/athlete/"+str(i)])
   retcode = subprocess.call(["wget", "--tries=100", "--retry-connrefused","--output-document=leaderboard-"+str(division)+"-"+str(i), "http://games.crossfit.com/scores/leaderboard.php?stage=5&sort=0&page="+str(i)+"&division="+str(division)+"&numberperpage=60&competition=0&frontpage=0&expanded=0&year=13&full=0&showtoggles=1&hidedropdowns=1&showathleteac=0&="])
   print(i)
   i=i+1





