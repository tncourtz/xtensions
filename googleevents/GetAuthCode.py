import requests
import json
from random import random
import urllib.parse
import shutil
import os





def GetAccessTokenJson():
    with open("./accesstoken.json", "r") as accesstokenfile:
        accessTokenJson = json.load(accesstokenfile)
        return accessTokenJson

def GetAccessToken():
    accessTokenJson = GetAccessTokenJson()
    accessToken = accessTokenJson['access_token']
    return  accessToken

def GetRefreshToken():
    refreshtokenfilename = "./refresh_token.json"
    if not os.path.isfile(refreshtokenfilename) or not os.access(refreshtokenfilename, os.R_OK):
        return None
    
    with open("./refresh_token.json", "r") as refreshtokenfile:
        refreshtokenjson = json.load(refreshtokenfile)
        return refreshtokenjson['refresh_token']

def LoadClientDetails():
    with open("./ClientDetailsApp.json", "r") as clientDetailsfile:
        clientDetailsJson = json.load(clientDetailsfile)
        return clientDetailsJson["web"]

def main():
    # TODO: It would be nice if we checked if the access token is really not valid before getting a new one with the refresh token.

    shutil.copyfile("./accesstoken.json", "./accesstoken.json.backup")

    cd = LoadClientDetails()
    refreshtoken = GetRefreshToken()
    if refreshtoken != None:
        requestData={
            "client_id": cd["client_id"],
            "client_secret": cd["client_secret"],
            "grant_type": "refresh_token",
            "refresh_token": refreshtoken
            }

        response = requests.post("https://oauth2.googleapis.com/token", data=requestData)
        f = open("./accesstoken.json", "wb")
        f.write(response.content)
        f.close()
        print ("Received the following body:")
        print (response.content)
    else:
        redirecturi = cd["redirect_uris"][0]
        clientid = cd["client_id"]
        authurl=f"https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www.googleapis.com/auth/drive&access_type=offline&include_granted_scopes=true&response_type=code&prompt=consent&redirect_uri={redirecturi}&client_id={clientid}"
        print (f"We don't have a refresh token. Please go to: {authurl}")


if __name__ == '__main__':
    main()
