import json
import requests
import re

import services.common.tools

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

def list(args):

    # List all kinds
    response = requests.post(
        services.common.tools.single_transaction_url(),
        auth=services.common.tools.credentials(),
        data=json.dumps({
            'statements': [{
                    'statement': "MATCH (n:Identifier) RETURN DISTINCT n.kind ORDER BY n.kind" }]}),
                  headers={'Content-Type': 'application/json',
                           'Accept': 'application/json; charset=UTF-8'})

    # Raise exception on bad HTTP status
    response.raise_for_status()

    # This needs some error handling. What if the remote source doesn't return JSON or times out?
    try:
        for result in response.json()['results'][0]['data']:
            print json.dumps({
                'class': 'identifier_kind',
                'id': result['row'][0],
                'name': result['row'][0],
                'url': ''}, indent=4)
            print '---'
    except ValueError:
        raise Exception('Not a JSON object: {}'.format(response.text))

def search(args):
    raise Exception('Not implemented yet')
