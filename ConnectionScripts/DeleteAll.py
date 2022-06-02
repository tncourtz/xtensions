import requests
import json
import logging
from urllib.parse import urljoin


apiManagerURL = "https://us.nintextest.io"
tenantURL = "https://ntx-xtn.workflowcloud-test.com"


def getAccessToken():
    sessionCookie=None
    with open("sessioncookie.json") as cookiefile:
        sessionCookie=json.load(cookiefile)

    if sessionCookie is None:
        raise Exception("Couldn't read sessioncookie from file.")

    genTokenURL = urljoin(tenantURL, "/generate-token")
    tokenResponse = requests.get(genTokenURL, cookies=sessionCookie)

    if tokenResponse.status_code == 200:
        tokenJson = json.loads(tokenResponse.text)
        return tokenJson["token"]

    raise Exception(f"Failed to retrieve token from {genTokenURL}")


def main():
    logging.basicConfig(
        encoding='utf-8',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)8s %(module)s (%(funcName)s): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )
    try:
    
        token = getAccessToken()
        connectionsURL = urljoin(apiManagerURL, "/designer_/api/connection/api/connections")
        headers={"authorization": "Bearer "+token}
        cons = requests.get(connectionsURL, headers=headers)

        allConnections = json.loads(cons.text)
        for con in allConnections:
            print (con)
            displayname = con["displayName"]
            deleteURL = urljoin(apiManagerURL, "/designer_/api/connections/", con["id"])
# NOT TESTED             requests.delete(deleteURL, headers=header)



    except KeyboardInterrupt:
        logging.info("You've hit ctrl+c, didn't you?")



if __name__ == '__main__':
    main()

