import requests
import json
from random import random

def GetAccessToken():
    with open("./accesstoken.json", "r") as accesstokenfile:
        accessTokenJson = json.load(accesstokenfile)
        
        accessToken = accessTokenJson['access_token']
        return  accessToken



def GetDrives():
    access_token = GetAccessToken()

    drives = []
    nextpage = None
    while True:
        url = "https://www.googleapis.com/drive/v3/drives?pageSize=100&useDomainAdminAccess=true"
        if nextpage != None:
            url = f"https://www.googleapis.com/drive/v3/drives?pageSize=100&pageToken={nextpage}&useDomainAdminAccess=true"

        response = requests.get(url, headers={'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(access_token)})
        if response.status_code != 200:
            print(f"Failed to retrieve drives!!!: {response.status_code}")
            print(response.content)
            return


        jsonResponse = json.loads(response.content)

        for drive in jsonResponse['drives']:
            drives.append(drive)
        if "nextPageToken" in jsonResponse:
            nextpage = jsonResponse['nextPageToken']
            print(f"Got Drives: {nextpage} - {len(jsonResponse['drives'])}")
        else:
            break
        
    return drives

def CreateDrive(driveName):
    access_token = GetAccessToken()
    
    response = requests.post(f"https://www.googleapis.com/drive/v3/drives?requestId={random()}" , 
        headers={'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(access_token)},
        json={"name": driveName})


    if response.status_code != 200:
        print(f"Failed to create drive: {response.status_code}")
        print(response.content)
        return

    print("Created drive!")
    print(json.loads(response.content))


def DeleteDrive(driveId):
    access_token = GetAccessToken()


    response = requests.delete(f"https://www.googleapis.com/drive/v3/drives/{driveId}?allowItemDeletion=true&useDomainAdminAccess=true" , 
        headers={'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(access_token)})
    

    if response.status_code != 204:
        print(f"Failed to delete drive {driveId}: {response.status_code}")
        print(response.content)
        return

    print("Drive Deleted!")


def main():
    drives = GetDrives()
    for drive in drives:
        drivename = drive['name']
        driveid = drive['id']
        print(f"{drivename} - {driveid}")
        if drivename[0:4] == "RDA_":
            DeleteDrive(driveid)


if __name__ == '__main__':
    main()
