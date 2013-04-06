from bs4 import BeautifulSoup
import sys
import subprocess


#Filename=sys.argv[1]

trav=1
totalWrite=""
toWrite=""

while (trav<226000):

        trav=trav+1
        if (trav==7): 
            trav=8

        Filename=str(trav)
        
        if ((trav%1000)==0):
   	    print("Filename = " + Filename)
        
        pageText = ""        
        try:
      	    pageText = open("./"+Filename, 'r').read()
        except IOError:
            return_code = subprocess.call("python get-athletes.py "+str(trav)+" "+str(trav+1), shell=True)
            #os.system("python get-athletes.py "+str(trav)+" "+str(trav+1))
      	    pageText = open("./"+Filename, 'r').read()
            print("Couldn't find file.")

	pageSoup = BeautifulSoup(pageText)

	pageText=pageSoup.get_text().encode('ascii', 'ignore')

	pageText=pageText[950:1500]

	#print(pageText)

	AthletePos=pageText.find('Athlete:', 1)
	EOLPos=pageText.find('\n',AthletePos)
	RegionPos=pageText.find('Region:', AthletePos)
	TeamPos=pageText.find('Team:', AthletePos)
	AffiliatePos=pageText.find('Affiliate:', AthletePos)
	GenderPos=pageText.find('Gender:', AthletePos)
	AgePos=pageText.find('Age:', AthletePos)
	HeightPos=pageText.find('Height:', AgePos)
	WeightPos=pageText.find('Weight:', AgePos)
	FranPos=pageText.find('Fran', AgePos)
	HelenPos=pageText.find('Helen', AgePos)
	GracePos=pageText.find('Grace', AgePos)
	Filthy50Pos=pageText.find('Filthy 50', AgePos)
	FightGBPos=pageText.find('Fight Gone Bad', AgePos)
	Sprint400mPos=pageText.find('Sprint 400m', AgePos)
	Run5kPos=pageText.find('Run 5k', AgePos)
	CleanJerkPos=pageText.find('Clean & Jerk', AgePos)
	SnatchPos=pageText.find('Snatch', AgePos)
	DLPos=pageText.find('Deadlift', AgePos)
	BackSquatPos=pageText.find('Back Squat', AgePos)
	MaxPullupsPos=pageText.find('Max Pull-ups', AgePos)

	toWrite=toWrite+str(Filename)+","

	#ATHLETE NAME
	toWrite=toWrite+pageText[AthletePos+9:EOLPos]+","

	if (TeamPos<0):
	    TeamPos=9999

	if (AffiliatePos<0):
	    AffiliatePos=9999

	#REGION
	toWrite=toWrite+pageText[RegionPos+7:min(GenderPos,TeamPos,AffiliatePos)]+","

	#TEAM
	toWrite=toWrite+pageText[TeamPos+5:min(AffiliatePos, GenderPos)]

	#NOT MISSING TEAM
	if (TeamPos<9998):    
	    toWrite=toWrite+pageText[TeamPos+7:TeamPos]+","
	else:
	    toWrite=toWrite+","

	#NOT MISSING AFFILIATE
	if (AffiliatePos<9998):
	    toWrite=toWrite+pageText[AffiliatePos+10:GenderPos]+","
	else:
	    toWrite=toWrite+","   

	#GENDER
	toWrite=toWrite+pageText[GenderPos+7:AgePos]+","

	#AGE
	toWrite=toWrite+pageText[AgePos+4:HeightPos]+","

	#HEIGHT
	toWrite=toWrite+pageText[HeightPos+7:WeightPos]+","

	#WEIGHT
	toWrite=toWrite+pageText[WeightPos+7:pageText.find('Bench',WeightPos)]+","

	#FRAN
	toWrite=toWrite+pageText[FranPos+4:HelenPos]+","

	#HELEN
	toWrite=toWrite+pageText[HelenPos+5:GracePos]+","

	#GRACE
	toWrite=toWrite+pageText[GracePos+5:Filthy50Pos]+","

	#FILTHY 50
	toWrite=toWrite+pageText[Filthy50Pos+9:FightGBPos]+","

	#FGB
	toWrite=toWrite+pageText[FightGBPos+14:Sprint400mPos]+","

	#Sprint 400m
	toWrite=toWrite+pageText[Sprint400mPos+11:Run5kPos]+","

	#Run 5k
	toWrite=toWrite+pageText[Run5kPos+6:pageText.find('Maxes',Run5kPos)]+","

	#C&J
	toWrite=toWrite+pageText[CleanJerkPos+12:SnatchPos]+","
		
	#Snatch
	toWrite=toWrite+pageText[SnatchPos+6:DLPos]+","

	#DL
	toWrite=toWrite+pageText[DLPos+8:BackSquatPos]+","

	#BS
	toWrite=toWrite+pageText[BackSquatPos+10:MaxPullupsPos]+","

	#Pullups
	toWrite=toWrite+pageText[MaxPullupsPos+12:pageText.find('Bio')]

	if (pageText.find('Athlete: Not found')<0):
	     #print(str(pageText.find('Athlete: Not found')))
             print(toWrite)
      	     totalWrite=totalWrite+"\n"+toWrite
        
        toWrite=""
else:
    with open("./processed-athletes-data.csv", "a") as f:
	f.write(totalWrite+"\n")
	f.close()


