#!/bin/bash

# This script will create a oAuth URL based on the details in `ClientDetailsApp.json` which is what you can download/export from google consokle.
# The URL it provides should be opened in the browser. The redirect URI should point to the /token.py endpoint (!)


CLIENTID=`cat ClientDetailsApp.json | jq -r '.web.client_id'`
REDIRECT_URI=`cat ClientDetailsApp.json | jq -r '.web.redirect_uris[0]'`


URL="https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www.googleapis.com/auth/drive&access_type=offline&include_granted_scopes=true&response_type=code&redirect_uri=${REDIRECT_URI}&client_id=${CLIENTID}"


echo "Please go to: "
echo ${URL}


