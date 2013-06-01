from bs4 import BeautifulSoup
import sys
import subprocess


FilenameAthletes=sys.argv[1]
FilenameScores=sys.argv[2]
FilenameOutput=sys.argv[3]

#print("Filename = " + Filename)

AthleteText = open(FilenameAthletes, 'r').read().encode('ascii', 'ignore')
ScoresText= open(FilenameScores, 'r').read().encode('ascii', 'ignore')

athleteTraverse=0

while (athleteTraverse<len(AthleteText)):
#while (athleteTraverse<2500):
     currentID=AthleteText[athleteTraverse:AthleteText.find(',',athleteTraverse)]
     #print("Current ID: " + str(currentID))
     scoreTraverse=ScoresText.find("\n"+str(currentID)+",")
     #print("Score Pos: " + str(scoreTraverse))
     #print("Score Text: " + ScoresText[scoreTraverse:ScoresText.find("\n",scoreTraverse)])
     #print("AthTraverse: " + str(athleteTraverse))
     
     nextScoreComma=ScoresText.find(",",scoreTraverse)
     nextScoreComma=ScoresText.find(",",nextScoreComma+1)
     
     remainScoreText=ScoresText[nextScoreComma:ScoresText.find("\n",nextScoreComma)]
 
     eolAthlete=AthleteText.find('\n',athleteTraverse)    
     
     #print("SCORE TRAVERSE: "+str(scoreTraverse))
     if (scoreTraverse==-1):
         remainScoreText=",-1,-1,-1,-1,-1,-1,-1,-1,-1,-1"
     AthleteText=AthleteText[:eolAthlete]+remainScoreText+AthleteText[eolAthlete:]

     print("AthText: " + AthleteText[athleteTraverse:AthleteText.find("\n",athleteTraverse)]+"\n")

     athleteTraverse=AthleteText.find('\n',athleteTraverse)+1

#print(AthleteText)

with open(sys.argv[3], "w") as f:
     f.write(AthleteText+"\n")
     f.close()



#AthletePos=pageText.find('Athlete:', 1000)
#EOLPos=pageText.find('\n',AthletePos)
#RegionPos=pageText.find('Region:', AthletePos)
#TeamPos=pageText.find('Team:', AthletePos)
#AffiliatePos=pageText.find('Affiliate:', AthletePos)
#GenderPos=pageText.find('Gender:', AthletePos)
#AgePos=pageText.find('Age:', AthletePos)
#HeightPos=pageText.find('Height:', AgePos)
#WeightPos=pageText.find('Weight:', AgePos)
#FranPos=pageText.find('Fran', AgePos)
#HelenPos=pageText.find('Helen', AgePos)
#GracePos=pageText.find('Grace', AgePos)
#Filthy50Pos=pageText.find('Filthy 50', AgePos)
#FightGBPos=pageText.find('Fight Gone Bad', AgePos)
#Sprint400mPos=pageText.find('Sprint 400m', AgePos)
#Run5kPos=pageText.find('Run 5k', AgePos)
#CleanJerkPos=pageText.find('Clean & Jerk', AgePos)
#SnatchPos=pageText.find('Snatch', AgePos)
#DLPos=pageText.find('Deadlift', AgePos)
#BackSquatPos=pageText.find('Back Squat', AgePos)
#MaxPullupsPos=pageText.find('Max Pull-ups', AgePos)

#toWrite=str(Filename)+", "


#if (pageText.find('Athlete: Not found')<0):
#     print(toWrite)
#     with open("./processed-athletes-data.csv", "a") as f:
#          f.write(toWrite+"\n")
#          f.close()


