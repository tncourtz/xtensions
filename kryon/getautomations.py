from urllib.parse import parse_qs
import json
import logging



def RunMe(urlObject = None):
    
    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug(qs)
    
    root = [
        {
            "path": "/Folder 1",
            "name": "Folder 1",
            "type": "folder"
        },
        {
            "path": "/Folder 2",
            "name": "Folder 2",
            "type": "folder"
        },
        {
            "path": "/Folder 3",
            "name": "Folder 3",
            "type": "folder"
        },
        {
            "path": "/My First Automation",
            "name": "My First Automation",
            "type": "file"
        }
    ]

    folder1 = [
        {
            "path": "/Folder 1/Folder 1",
            "name": "Folder 1.1",
            "type": "folder"
        },
              {
            "path": "/Folder 1/Folder 2",
            "name": "Folder 1.2",
            "type": "folder"
        },
        {
            "path": "/Folder 1/My second Automation",
            "name": "My second Automation",
            "type": "file"
        }
       
    ]


    folder2 = [
        {
            "path": "/Folder 2/Folder 1",
            "name": "Folder 2.1",
            "type": "folder"
        },
              {
            "path": "/Folder 2/Folder 2",
            "name": "Folder 2.2",
            "type": "folder"
        },
        {
            "path": "/Folder 2/2.2. My 3rd Automation",
            "name": "2.2. My 3rd Automation",
            "type": "file"
        }
       
    ]


    if "currentPath" in qs:
        if qs["currentPath"][0] == "/Folder 1":
            return json.dumps(folder1)
        if qs["currentPath"][0] == "/Folder 2":
            return json.dumps(folder2)

    return json.dumps(root)
    
    