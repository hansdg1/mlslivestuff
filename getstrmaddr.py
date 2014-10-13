#!/usr/bin/python
import sys,urlparse,urllib2
#URL=sys.argv[1]
#example http://nlds108.cdnak.neulion.com/nlds/mls/sportingkansascity/as/live/sportingkansascity_hd_3000.m3u8
index=0
top=200
team=sys.argv[1]
#team="realsaltlake"
count=1
#tryurl="http://nlds"+index+".cdnak.neulion.com/nlds/mls/"+team+"/as/live/"+team+"_hd_3000.m3u8"

while(count<top):
 index=str(int(index) + 1)
 try:
#  print count
  tryurl="http://nlds"+index+".cdnak.neulion.com/nlds/mls/"+team+"/as/live/"+team+"_hd_3000_ced.m3u8"
  if (urllib2.urlopen(tryurl).code == 200):
   print "Exists!"
   print tryurl
 except urllib2.HTTPError:
  pass
 count+=1
