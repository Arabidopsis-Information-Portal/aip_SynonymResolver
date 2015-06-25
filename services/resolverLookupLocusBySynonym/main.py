import json
import requests
import re

import services.common.tools

# aip/resolverLookupLocusBySynonym
#
# Given any (known) name for a locus, resolve the name to that locus

# Future work: Refactor this to use a cascade of approaches
# and to fail gracefully if we can't figure it out
# For the Interaction viewer, if it is returning intact: namespace this means it can't resolve to anything
# Search order: UniProt resolver; maybe EBI PICR (http://www.ebi.ac.uk/Tools/picr/RESTDocumentation.do); Local

def search(arg):

    # syn is the synonym being interrogated
    syn = arg['identifier']

    # Client was not supposed to send a valid AGI locus
    # If he did, invoke backend query differently
    p = re.compile('AT[1-5MC]G[0-9]{5,5}', re.IGNORECASE)
    if not p.search(syn):
        payload = json.dumps({
'statements': [{
'statement': "MATCH (a:Identifier { name:'%s' })-[:SYNONYM_OF*1..2]-(x:Identifier) WHERE x.kind IN ['TAIR'] return DISTINCT x.name, a.kind ORDER BY x.name" %(syn,) }]})
    else:
        payload = json.dumps({'statements': [{'statement': "MATCH (a:Identifier { name:'%s' }) WHERE a.kind IN ['TAIR'] RETURN a.name, a.kind" %(syn,) }]})

    # Send the query
    response = requests.post( services.common.tools.single_transaction_url(),
        auth=services.common.tools.credentials(),
        data=payload,
        headers={'Content-Type': 'application/json','Accept': 'application/json; charset=UTF-8'})

    # Raise exception on bad HTTP status
    response.raise_for_status()

    # Stream back the results
    try:
        for result in response.json()['results'][0]['data']:
            print json.dumps({
            'class': 'locus_id_mapping',
            'locus': result['row'][0],
            'relationships': [{'type': 'synonymous_with', 'direction': 'undirected', 'scores': [{'confidence': 1.00 }]}],
            'related_entity': syn,
            'related_entity_kind':result['row'][1]})
            print '---'
    except ValueError:
        raise Exception('Not a JSON object: {}'.format(response.text))

def list(args):
    raise Exception('Not implemented yet')
