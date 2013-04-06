from bs4 import BeautifulSoup
import sys
import subprocess


FilenameAthletes=sys.argv[1]
FilenameOutput=sys.argv[2]

#print("Filename = " + Filename)

AthleteText = open(FilenameAthletes, 'r').read().encode('ascii', 'ignore')

athleteTraverse=0
#athleteTraverse=1850000

print("Total Length: " + str(len(AthleteText)))

while (athleteTraverse<len(AthleteText)):
#while (athleteTraverse<500000):

    nextComma=AthleteText.find(',',athleteTraverse)+1
    currentString=AthleteText[athleteTraverse:nextComma]

    if (currentString.find('ossFit 27:17')>0):
         currentString="crossfit 27-17,"
         athleteTraverse=athleteTraverse+14

    if (currentString.find('ossFit 4:13')>0):
         currentString="crossfit 4-13,"
         athleteTraverse=athleteTraverse+14

    if (currentString.find('ville: The Anvil')>0):
         currentString="Crossfit Summerville- The Anvil,"
         athleteTraverse=athleteTraverse+25

    # find lb and convert to kg
    if (currentString.find(' lb,')>-1):
         locationOfUnit=currentString.find('lb')
         remainString=currentString[:locationOfUnit]
         
         intValue=int(remainString)
         newValue=int(round(intValue/2.2))

         #print(str(athleteTraverse)+"  "+ str(newValue))

 
         AthleteText=AthleteText[:athleteTraverse]+str(newValue)+","+AthleteText[nextComma:]

    # find and remove " cm"
    if (currentString.find(' cm,')>-1):
         #print("REMOVED CM" + str(currentString))
         locationOfUnit=currentString.find(' cm')
         remainString=currentString[:locationOfUnit]
         
         #print(str(athleteTraverse)+"  "+ str(newValue))

         AthleteText=AthleteText[:athleteTraverse]+remainString+AthleteText[nextComma-1:]

    # find and remove " kg"
    if (currentString.find(' kg,')>-1):
         #print("REMOVED KG" + str(currentString))
         locationOfUnit=currentString.find(' kg')
         remainString=currentString[:locationOfUnit]
         
         #print(str(athleteTraverse)+"  "+ str(newValue))

         AthleteText=AthleteText[:athleteTraverse]+remainString+AthleteText[nextComma-1:]

    # find inches and convert to cm
    if ((currentString.find('\'')>-1) and (currentString.find('\"')>-1)):
         locationOfSingleQuote=currentString.find('\'')
         remainString=currentString[:locationOfSingleQuote]
         
         intValue=int(remainString)
         feetValue=int(round(intValue*12))

         locationOfDoubleQuote=currentString.find('\"')
         remainString=currentString[locationOfSingleQuote+1:locationOfDoubleQuote]
         
         intValue=int(remainString)
         inchesValue=int(intValue)

         totalInches=feetValue+inchesValue

         #print("Total Inches: " + str(totalInches))

         AthleteText=AthleteText[:athleteTraverse]+str(int(round(totalInches*2.54)))+","+AthleteText[nextComma:]

    # find minutes and convert to seconds
    if ((currentString.find(':')>-1) and (currentString.find('oss')<0)):

         locationOfColon=currentString.find(':')
         remainString=currentString[:locationOfColon]
         
         intValue=int(remainString)
         minuteValue=int(round(intValue*60))

         secondsValue=int(currentString[(currentString.find(':')+1):len(currentString)-1])

         totalSeconds=minuteValue+secondsValue

         #print("Total Seconds: " + str(totalSeconds))

         AthleteText=AthleteText[:athleteTraverse]+str(totalSeconds)+","+AthleteText[nextComma:]
        
    if (athleteTraverse%20000<1):
         percentage=float(athleteTraverse*100/len(AthleteText))
         #print(len(AthleteText))
         print(str(athleteTraverse)+ "-" +str(percentage)+"%")
 
    athleteTraverse=athleteTraverse+1
    #athleteTraverse=nextComma+1

AthleteText="ID,NAME,REGION,TEAM,AFFILIATE,GENDER,AGEyrs,HEIGHTcm,WEIGHTkg,FRANsec,HELENsec,GRACEsec,FILTHY50sec,FIGHTGONEBAD,SPRINT400Msec,RUN5Ksec,CLEANJERKkg,SNATCHkg,DEADLIFTkg,BACKSQUATkg,MAXPULLUPS,13-1Rank,13-1Score,13-2Rank,13-2Score,13-3Rank,13-3Score,13-4Rank,13-4Score,13-5Rank,13-5Score"+AthleteText

with open(sys.argv[2], "w") as f:
     f.write(AthleteText+"\n")
     f.close()


