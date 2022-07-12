from urllib.parse import parse_qs
import json
import os
import logging
import time



def RunMe(urlObject = None):
    
    

    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug("INPUT:")
    logging.debug(qs)



    # Some default props we always want to have
    props = {}
    for var in ["ExcelFileLocation", "InputCell1", "MyOutputValue"]:
        props[var] = { "type": "string" }
 
    props = {}
    

    if "automation" in qs and qs["automation"][0]:
        autoname = qs["automation"][0]
        autovarfile = "kryon/automationvariables/" + autoname + ".txt"
        logging.debug(f"Trying to get file for automation {autoname} in {autovarfile}")

        if "test2" in autoname:
            sleeptime = 2
            logging.info(f"Sleeping for {sleeptime} seconds")
            time.sleep(sleeptime)
            logging.debug("Done snoozing")
        if os.path.exists(autovarfile):
            with open(autovarfile) as f:
                variables = f.readlines()
                props = {}
                for line in variables:
                    line = line.strip()
                    props[line] = { "type": "string"}
        else:
            logging.debug(f"File {autovarfile} not found.")

    defaultautomation = {
        "stuff": { 
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": props,
        }
    }


    return json.dumps(defaultautomation)