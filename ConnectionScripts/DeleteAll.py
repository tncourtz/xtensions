import requests
import json
import logging
from urllib.parse import urljoin


apimURL = "https://eu.nintex.io"


def getAccessToken():
    with open("apimanager.token.json") as file:
        data = json.load(file)

    return data["access_token"]



def main():
    logging.basicConfig(
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)8s %(module)s (%(funcName)s): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )
    try:
    
        token = getAccessToken()
        connectionsURL = urljoin(apimURL, "/designer_/api/connection/api/connections")
        headers={"authorization": "Bearer "+token}
        cons = requests.get(connectionsURL, headers=headers)

        allConnections = json.loads(cons.text)
        for con in allConnections:
            print (con)
            displayname = con["displayName"]
            deleteURL = urljoin(apimURL, "/designer_/api/connections/", con["id"])
# NOT TESTED             requests.delete(deleteURL, headers=header)



    except KeyboardInterrupt:
        logging.info("You've hit ctrl+c, didn't you?")



if __name__ == '__main__':
    main()

