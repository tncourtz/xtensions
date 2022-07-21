from urllib.parse import parse_qs
import json
import os
import logging



def RunMe(urlObject = None):
    
    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug("INPUT:")
    logging.debug(qs)
    
    retval =  [
        { "path": "/First", "name": "First", "value": "/1", "type": "folder" },
        { "path": "/Second", "name": "Second", "value": "/2", "type": "folder" },
        { "path": "/2nd", "name": "2nd",  "value": "/3", "type": "folder" }
    ]

    if "currentitem" in qs:
        currentitem = qs["currentitem"][0]
        if currentitem == "/1":
            retval =  [
                { "path": "/First/myfile.txt", "name": "myfile.txt", "value": "/1/1", "type": "file" },
                { "path": "/First/myfile.txt", "name": "myfile.txt", "value": "/1/3", "type": "file" },
                { "path": "/First/MySecondFolder", "name": "MySecondFolder", "value": "/1/2", "type": "folder" },
            ]
        elif currentitem == "/2":
            retval =  [
                { "path": "/Second/myfile.txt", "name": "myfile.txt", "value": "/2/1", "type": "file" },
                { "path": "/Second/mything.txt", "name": "mything.txt", "value": "/2/2", "type": "file" },
            ]
        elif currentitem == "/3":
            retval =  [
                { "path": "/2nd/myfile.txt", "name": "myfile.txt", "value": "/3/1", "type": "file" },
                { "path": "/2nd/mything.txt", "name": "mything.txt", "value": "/3/2", "type": "file" },
            ]
        elif currentitem == "/1/2":
            retval =  [
                { "path": "/First/MySecondFolder/Onefile.txt", "name": "Onefile.txt", "value": "/1/2/3", "type": "file" },
                { "path": "/First/MySecondFolder/Twofile.txt", "name": "Twofile.txt", "value": "/1/2/4", "type": "file" }
            ]

    
    return json.dumps(retval)