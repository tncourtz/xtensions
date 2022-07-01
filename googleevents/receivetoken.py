from urllib.parse import parse_qs
import requests
import json
import logging



def RunMe(urlObject = None):
    
    

    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug("INPUT:")
    logging.debug(qs)

    code = qs['code']

    if code:
        appDetailsFile = open("./googleevents/ClientDetailsApp.json", "r");
        appDetails = json.load(appDetailsFile)
        appDetailsFile.close()

        requestData={
            "code": code, 
            "client_id": appDetails['web']['client_id'],
            "client_secret": appDetails['web']['client_secret'],
            "redirect_uri": appDetails['web']['redirect_uris'][0],
            "grant_type": "authorization_code"
            }

        response = requests.post("https://oauth2.googleapis.com/token", data=requestData)
        f = open("./googleevents/accesstoken.json", "wb")
        f.write(response.content)
        f.close()
        print ("Received the following body:")
        print (response.content)



    return "Thanks!"