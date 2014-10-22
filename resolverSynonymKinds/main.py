import json
import requests
import re
import resolver_common

# aip/resolverSynonymKinds
#
# Return a list of or query against kinds of identifiers
# Arguments: None
# Requires headers:
# Accept:application/json
# Content-Type:application/json

'''
{
  "statements" : [ {
    "statement" : "MATCH (n:Identifier) RETURN DISTINCT n.kind ORDER BY n.kind"
  } ]
}
'''

# Returns JSON objects, one per source. Name will eventually be a human-readable label
# but for now is the same as the id.

'''
{"id":"UniProt",
 "name:"Uniprot",
 "url":""}
'''

def list(arg):

    # List all kinds
    response = requests.post(
        resolver_common.single_transaction_url(),
        data=json.dumps({
            'statements': [{
                    'statement': "MATCH (n:Identifier) RETURN DISTINCT n.kind ORDER BY n.kind" }]}),
                  headers={'Content-Type': 'application/json',
                           'Accept': 'application/json; charset=UTF-8'})

    # This needs some error handling. What if the remote source doesn't return JSON or times out?
    for result in response.json()['results'][0]['data']:
        print json.dumps({
            'class': 'identifier_kind',
            'id': result['row'][0],
            'name': result['row'][0],
            'url': ''}, indent=4)
        print '---'

def search(arg):
    # Search for and return a specific kind. Not implemented at present.
    pass

def help(arg):
    # Placeholder for inline help presented in Markdown or other format
    pass
