#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

# Written by Alan Viars
import json, sys
from validate_basic import validate_basic_dict

def validate_pjson(j):
    """
    Input a JSON object as a string. return a list of errors. If error list
    is empty then the file is valid.
    """
    errors =[]
    
    # Does the string contain JSON 
    try:
        d = json.loads(j)
    except:
        error ="The string did not contain valid JSON."
        errors.append(error)
        return errors
    
    # Is it a dict {} (JSON object equiv)?
    if type(d)!=type({}):
        error ="The JSON string did not contain a JSON object i.e. {}."
        errors.append(error)
        return errors
    
    # Does it contain the top-level enumeration_type
    if not d.has_key("enumeration_type"):
        error ="The JSON object does not contain enumeration_type."
        errors.append(error)
        return errorso
    # Is the enumeration_type a valid?
    if d["enumeration_type"] not in ("NPI-1", "NPI-2", "OEID", "HPID"):
        error ="enumeration_type must be one of these: ('NPI-1', 'NPI-2', 'OEID', 'HPID')"
        errors.append(error)
        return errors
    
    #If a number is present we assume this is an update.
    if not d.has_key("number"):
        number = None
    else:
        number = d['number']
    
    
    #Check for errors in the basic section    
    basic_errors = validate_basic_dict(d['basic'], d['enumeration_type'], number)
    if basic_errors:
        errors = errors + basic_errors
    
    
    return errors


if __name__ == "__main__":

    if len(sys.argv)<2:
        print "You must suppy a ProviderJSON file to validate"
        print "Example: python validate.py [ProivderJSON]"
    else:
        pjson_file = sys.argv[1]
    
    #Open the file
    fh = open(pjson_file, 'r')
    
    j = fh.read()
    
    errors = validate_pjson(j)
    
    errors_json =  json.dumps(errors, indent =4)
    print errors_json
        
    
    
    