from urllib.parse import parse_qs
import json
import logging



def RunMe(urlObject = None):
    
    

    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug(qs)
    
    automation1props = {}
    automation2props = {}
    for var in ["ExcelFileLocation", "InputCell1", "MyOutputValue"]:
        automation1props[var] = { "type": "string" }
    for var in ["ExcelHTTPLocation", "SomeOthercell", "MyOutputValue"]:
        automation2props[var] = { "type": "string" }

    automation1 = {
        "stuff": { 
                "$schema": "http://json-schema.org/draft-04/schema#",
                "type": "object",
                "properties": automation1props,
                "required": ["ExcelFileLocation"] 
            }
        }
    automation2 = {
        "stuff": { 
                "$schema": "http://json-schema.org/draft-04/schema#",
                "type": "object",
                "properties": automation2props,
                "required": ["ExcelHTTPLocation", "SomeOtherCell" ]
            }
        }

    if "automation" in qs and qs["automation"][0]:
        return json.dumps(automation2)

    return json.dumps(automation1)