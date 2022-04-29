from urllib.parse import parse_qs
import json
import logging



def RunMe(urlObject = None):
    
    props = {}

    if (urlObject != None):
        qs = parse_qs(urlObject.query)
    logging.debug(qs)
    props["variable1"] = { "type": "string"}
    props["variable2"] = { "type": "string"}
    basicJson = {"stuff": { "$schema": "http://json-schema.org/draft-04/schema#"}, "type": "object", "properties": props }

    return json.dumps(basicJson)