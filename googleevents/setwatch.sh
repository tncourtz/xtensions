#!/bin/bash

ACCESS=`jq -r '.access_token' accesstoken.json `

NOW=`date +%s`
EXP=`expr ${NOW} + 3600`
EXP=`expr ${EXP} '*' 1000`

SETWATCH=$( jq -n \
	--arg exp "$EXP" \
	'{
		"id": "5",
		"type": "web_hook",
		"token": "MyWatchToken=1",
		"address": "https://dev.prof-x.net/googleappnotification/",
		"expiration": $exp
	}'
	)

echo $SETWATCH > postdata.txt


## This sets a watch on a file/folder. You then *ONLY* get updates to that item. if it's a folder, a new file created does NOT raise an event.
# curl -d @postdata.txt -H "Authorization: Bearer ${ACCESS}" -H 'Content-Type: application/json' "https://www.googleapis.com/drive/v3/files/1UVYmCDXFHeoEqJhmJ5heQUMaVHCPEUaO/watch?fields=id,kind&supportsAllDrives=true"  > setwatchresponse.json


## Stop it..
# curl -d '{ "id": "5", "resourceId": "-9hsprrBSp6LKyijAJftwc713dU"}' -H "Authorization: Bearer ${ACCESS}" -H 'Content-Type: application/json' "https://www.googleapis.com/drive/v3/channels/stop"




## This adds a channel watch, which gets you lots of info...
curl -H "Authorization: Bearer ${ACCESS}" "https://www.googleapis.com/drive/v3/changes/startPageToken?supportsAllDrives=true" > startpagetokenresponse.json
PAGETOKEN=`cat startpagetokenresponse.json  | jq -r '.startPageToken'`
curl -d @postdata.txt -H "Authorization: Bearer ${ACCESS}" -H 'Content-Type: application/json' "https://www.googleapis.com/drive/v3/changes/watch?fields=id,kind&supportsAllDrives=true&pageToken=${PAGETOKEN}"  > setwatchresponse.json