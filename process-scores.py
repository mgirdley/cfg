from bs4 import BeautifulSoup
import sys
import subprocess


Filename=sys.argv[1]
print("Filename = " + Filename)

pageText = open(Filename, 'r').read()

pageSoup = BeautifulSoup(pageText)

#pageText=pageSoup.get_text().encode('ascii', 'ignore')

#print(pageText)

scoreTag = pageSoup.findAll("td", {"name"})

for result in scoreTag:
     #print("Athlete Name: " + str(result))
     athleteLink=result.find_next("a")
     #print(athleteLink)
     #print(athleteLink['href'])
     athleteLink=athleteLink['href']
     athleteID=athleteLink[athleteLink.rfind('/')+1:]
     #print("Athlete ID: " + athleteID)
     toWrite=athleteID+","
     #print("Athlete Name: " + result.getText())
     toWrite+=result.getText()
     nextScore=result.find_all_next("span", {"display"}, limit=5)
     for scores in nextScore:
          #print(scores.getText())
          tempScore=scores.getText()
          tempScore=tempScore[tempScore.find('(')+1:tempScore.find(')')]
          if (tempScore.find('--')==0):
               tempScore="0"
          #print("Score: " + str(tempScore))
          toWrite+="," + str(tempScore)
     print(toWrite)
     
     with open("./processed-score-data.csv", "a") as f:
          f.write(toWrite.encode('ascii', 'ignore')+"\n")
          f.close()


