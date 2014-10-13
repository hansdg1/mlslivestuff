#!/usr/bin/python

import sys,urlparse,re

#single first var
TEAMSREGEX='\-\D{2,3}\-v-\D{2,3}\/'
dateregex='\d{4}\-\d{2}\-\d{2}'
#example url
# http://nlds14.neulion.com/nlds_vod/mls/vod/2013/10/19/485079/2_485079_rsl_por_2013_h_whole_1_3000.mp4

#urlparse
#path = urlparse.urlparse(sys.argv[1])
#print(path.path)

URL=raw_input("Match URL: ")
#MATCHID=sys.argv[2]
MATCHID=str(input("Match ID: "))

#URL=sys.argv[1]
if re.search(dateregex,URL):
 result=re.search('\d{4}\-\d{2}\-\d{2}',URL)
 date=result.group().replace('-',' ').split(' ')
# print(date[1])
# if re.search('\D{3}\-v-\D{3}',URL):

#live url http://live.mlssoccer.com/mlsmdl/match/2013-11-10-RSL-v-POR/1364
if re.search(TEAMSREGEX,URL):
 result2=re.search(TEAMSREGEX,URL)
 TEAMSARR=result2.group().replace('-','').replace('/','').split('v')
 TEAMS_STR=TEAMSARR[1]+'_'+TEAMSARR[0]
 TEAMS_STR=TEAMS_STR.lower()
 print(TEAMSARR) #.group()
#TEAMS="por_rsl"
wc="whole"
quality="3000"
URL="http://nlds14.neulion.com/nlds_vod/mls/vod/"+date[0]+"/"+date[1]+"/"+date[2]+"/"+MATCHID+"/2_"+MATCHID+"_"+TEAMS_STR+"_"+date[0]+"_h_"+wc+"_1_"+quality+".mp4"
print(URL)
