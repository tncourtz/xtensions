#!/bin/bash

ACCESS=`jq -r '.access_token' accesstoken.json `

NOW=`date +%s`
EXP=`expr ${NOW} + 3600`
EXP=`expr ${EXP} '*' 1000`

PAGETOKEN=0

if test -f "getchangesresponse.json"; then
    echo "Getting pagetoken from getchangesresponse.json"
    PAGETOKEN=`jq -r '.newStartPageToken' getchangesresponse.json`
else
    if test -f "startpagetokenresponse.json"; then
        echo "Getting page token from startpagetokenresponse.json"
        PAGETOKEN=`jq -r '.startPageToken' startpagetokenresponse.json`
    fi
fi

if [ $PAGETOKEN == 0 ]; then
    echo "No page token."
    exit
fi

curl -H "Authorization: Bearer ${ACCESS}" \
     -H 'Content-Type: application/json' \
     "https://www.googleapis.com/drive/v3/changes?driveId=0APzXdF6L45tIUk9PVA&includeItemsFromAllDrives=true&supportsAllDrives=true&pageToken=${PAGETOKEN}&fields=*" > getchangesresponse.json

