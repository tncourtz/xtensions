from urllib.parse import parse_qs
import json
import os
import logging



def RunMe(urlObject = None):
    
    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug("INPUT:")
    logging.debug(qs)
    
    splitted=[""]

    if "currentPath" in qs:
        splitted = list(filter(None, qs["currentPath"][0].split("/")))

    base = os.path.join("kryon", "automationvariables")

    if os.path.isdir(base):
        return json.dumps(findEnd(base, splitted, 0))
    else:
        return json.dumps({"failed", True })
    
        



    

def findEnd(base, pathbits, depth):
    logging.debug(f"findEnd({base},{pathbits},{depth}")
    logging.debug(f"Len: {len(pathbits)} - {depth}")
    if len(pathbits) == 0:
        return listDir(base)
    else:
        oneup = os.path.join(base, pathbits[depth])
    logging.debug(f"OneUp: {oneup}")
    if os.path.isdir(oneup):
        if depth == len(pathbits)-1:
            logging.debug("List the directory")
            dirlist = listDir(oneup)
            return dirlist
        else:
            depth = depth + 1
            return findEnd(oneup, pathbits, depth)
    if os.path.isfile(oneup):
        return json.dumps({"file", True})


def listDir(path):
    items = []
    if os.path.exists(path):
        for item in os.listdir(path):
            itempath = os.path.join(path, item)
            if os.path.isfile(itempath):
                obj = {
                    "path": itempath[len("kryon/automationvariables"):-4],
                    "name": item[0:-4],
                    "type": "file"
                }
                items.append(obj)
            elif os.path.isdir(itempath):
                obj = {
                    "path": itempath[len("kryon/automationvariables"):],
                    "name": item,
                    "type": "folder"
                }
                items.append(obj)
    logging.debug(items)
    return items


