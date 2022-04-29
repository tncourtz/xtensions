from urllib.parse import parse_qs
import json
import logging



def RunMe(urlObject = None):
    
    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug(qs)
    
    automation1 = [
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

    automation2 = [
        {
            "variablename": "ExcelHTTPLocation",
        },
        {
            "variablename": "SomeOthercell",
        },
        {
            "variablename": "MyOutputValue",
        }    
    ]



    if "automation" in qs and qs["automation"][0]:
        return json.dumps(automation2)

    return json.dumps(automation1)
    
    