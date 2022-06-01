from email import header
from venv import create
import requests
import json
import logging
from urllib.parse import urljoin


apimURL = "https://us.nintextest.io"


def getAccessToken():
    with open("apimanager.token.json") as file:
        data = json.load(file)

    return data["access_token"]

def getConnections():
    with open("connectionlist.json") as file:
        data = json.load(file)
    return data



def main():
    logging.basicConfig(
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)8s %(module)s (%(funcName)s): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )
    try:
        token = getAccessToken()
        connections = getConnections()
        
        headers={"authorization": "Bearer "+token}

        for con in connections:

            createurl = urljoin(apimURL,f'/connection/api/v1/connections?appId={con["AppId"]}')
            print(con["ConnectionDetails"])
            res = requests.post(createurl, json = con["ConnectionDetails"], headers=headers)
            print(res.text)

    except KeyboardInterrupt:
        logging.info("You've hit ctrl+c, didn't you?")



if __name__ == '__main__':
    main()