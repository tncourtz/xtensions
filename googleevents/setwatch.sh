#!/bin/bash

ACCESS=`jq -r '.access_token' accesstoken.json `

NOW=`date +%s`
EXP=`expr ${NOW} + 600`
EXP=`expr ${EXP} '*' 1000`

SETWATCH=$( jq -n \
	--arg exp "$EXP" \
	'{
		"kind": "api#channel",
		"id": "FFFFF-cf8f-4798-961b-10a0b73af2BB",
		"type": "web_hook",
		"token": "myId=1&Folder=test",
		"expiration": $exp,
		"address": "https://dev.prof-x.net/googleappnotification/",
		"payload": true
	}'
	)

echo $SETWATCH > postdata.txt







## This adds a channel watch, which gets you lots of info...
curl -H "Authorization: Bearer ${ACCESS}" "https://www.googleapis.com/drive/v3/changes/startPageToken?supportsAllDrives=true" > startpagetokenresponse.json
PAGETOKEN=`cat startpagetokenresponse.json  | jq -r '.startPageToken'`

## All changes
curl -d @postdata.txt -H "Authorization: Bearer ${ACCESS}" -H 'Content-Type: application/json' "https://www.googleapis.com/drive/v3/changes/watch?fields=*&driveId=0APzXdF6L45tIUk9PVA&includeItemsFromAllDrives=true&supportsAllDrives=true&pageToken=1"  > setwatchresponse.json


## Specific object changes.- this only works correclty on MyDrive items - https://issuetracker.google.com/issues/130736018
# curl -d @postdata.txt -H "Authorization: Bearer ${ACCESS}" -H 'Content-Type: application/json' "https://www.googleapis.com/drive/v3/files/1lY3D3oN4ItpZGtOgF1vhQ8FDadDDlBQi/watch?fields=*"  > setwatchresponse.json


## Stopping it can be done as such.
# curl -d '{ "id": "FFFFF-cf8f-4798-961b-10a0b73af2BB", "resourceId": "w4RzAbNsy46h7Y02dHwxjTBPTJU"}' -H "Authorization: Bearer ${ACCESS}" -H 'Content-Type: application/json' "https://www.googleapis.com/drive/v3/channels/stop"
