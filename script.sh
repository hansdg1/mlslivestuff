## declare an array variable
bot=1
top=100
count=1
declare -a playoffteams=(sportingkc newyorkredbulls seattlesoundersfc houstondynamo philadelphiaunion sportingkansascity newenglandrevolution)
declare -a restofteams=(columbuscrew sanjoseearthquakes)
## now loop through the above array
for t in ${playoffteams[@]} 
do
  # echo $i # or do whatever with individual element of the array done
    DLURL="http://nlds$count.cdnak.neulion.com/nlds/mls/$t/as/live/$t\_hd_3000.m3u8" 
    #wget http://nlds{1..200}.cdnak.neulion.com/nlds/mls/$t/as/live/$t\_hd_3000.m3u8
    echo "$DLURL"
    wget -q "$DLURL"
#    wget -q "http://google.com/favicon.ico"
   if [ "$count" -lt "$top" ]; then
    if [ $? -ne 0 ] 
      then echo "not exist"
      #success
    fi
    else break
    let count+=1
   fi
done
# You can access them using echo ${arr[0]}, ${arr[1]} also
