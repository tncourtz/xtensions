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
        }   , 
        {
            "variablename": "MyOutputValue1",
        }    ,
        {
            "variablename": "MyOutputValue2",
        }    ,
        {
            "variablename": "MyOutputValue3",
        }    ,
        {
            "variablename": "MyOutputValue3",
        }    ,
        {
            "variablename": "MyOutputValue4",
        }    ,
        {
            "variablename": "MyOutputValue5",
        }    ,
        {
            "variablename": "MyOutputValue6",
        }    ,
        {
            "variablename": "MyOutputValue7",
        }    ,
        {
            "variablename": "MyOutputValue8",
        }    ,
        {
            "variablename": "MyOutputValue9",
        }    ,
        {
            "variablename": "MyOutputValue10",
        }    ,
        {
            "variablename": "MyOutputValue11",
        }    ,
        {
            "variablename": "MyOutputValue12",
        }    ,
        {
            "variablename": "MyOutputValue13",
        }    ,
        {
            "variablename": "MyOutputValue14",
        }    ,
        {
            "variablename": "MyOutputValue15",
        }    
    ]



    if "automation" in qs and qs["automation"][0]:
        return json.dumps(automation2)

    return json.dumps(automation1)
    
    