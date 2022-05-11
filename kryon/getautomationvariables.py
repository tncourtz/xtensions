from urllib.parse import parse_qs
import json
import os
import logging



def RunMe(urlObject = None):
    
    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug("INPUT:")
    logging.debug(qs)
    
    automationvars = [
        {
            "variablename": "ExcelFileLocation",
        },
        {
            "variablename": "InputCell1",
        },
        {
            "variablename": "MyOutputValue",
        }    
    ]





    
    if "automation" in qs and qs["automation"][0]:
        autoname = qs["automation"][0][1:]
        
        autovarfile = os.path.join("kryon", "automationvariables", autoname + ".txt")
        logging.debug(f"Trying to get file for automation {autoname} in {autovarfile}")
        if os.path.exists(autovarfile):
            with open(autovarfile) as f:
                variables = f.readlines()
                automationvars = []
                for line in variables:
                    line = line.strip()
                    prop = { "variablename": line }
                    automationvars.append(prop)
        else:
            logging.debug(f"File {autovarfile} not found.")


    return json.dumps(automationvars)
    
    