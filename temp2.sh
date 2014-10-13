#first argument is the match id
MATCHID=$1
#second argument is teams in teams in AWAY_HOME order

TEAMS=$}_${home}
DATE=2013/10/18
DLURL="http://nlds14.cdnak.neulion.com/nlds/mls/$t/as/live/$t\_hd_3000.m3u8"
#echo ${1} + $2 encapsulating variables inside of { } braces
#http://nlds14.neulion.com/nlds_vod/mls/vod/2013/10/18/485076/2_485076_dc_kc_2013_h_condensed_1_3000.mp4
echo "http://nlds14.neulion.com/nlds_vod/mls/vod/${DATE}/${MATCHID}/2_${MATCHID}_${TEAMS}_h_${wc}_1_${quality}.mp4"
