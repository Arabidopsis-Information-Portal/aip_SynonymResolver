import json
import requests
import re
import services.common.tools

# aip/resolverLookupSynonymsByLocus
#
# Given any known AGI locus, return the list of known synonyms
# Arguments
# query - STRING (mandatory)

def search(args):

# arg contains a dict with one key:value
#
# locus is gene identifier

    term = args['locus']
    term = term.upper()
    # Ensure term is a valid AGI locus
    p = re.compile('AT[1-5MC]G[0-9]{5,5}', re.IGNORECASE)
    if not p.search(term):
        raise Exception('Invalid query term')

    payload = json.dumps({'statements': [{
'statement': "MATCH (a:Identifier { name:'%s' })-[:SYNONYM_OF*1..2]-(x:Identifier) WHERE NOT x.kind IN ['TAIR', 'NCBI_TaxID'] return DISTINCT x.name, x.kind ORDER BY x.name" %(term,) }]})
    response = requests.post( services.common.tools.single_transaction_url(),
        auth=services.common.tools.credentials(),
        data=payload,
        headers={'Content-Type': 'application/json','Accept': 'application/json; charset=UTF-8'})

    # Raise exception on bad HTTP status
    response.raise_for_status()

    try:
        for result in response.json()['results'][0]['data']:
            print json.dumps({
			'class': 'locus_id_mapping',
			'related_entity': result['row'][0],
			'locus': term,
			'relationships': [{'type': 'synonymous_with', 'direction': 'undirected', 'scores': [{'confidence': 1.00 }] }],
			'related_entity_kind':result['row'][1]})
            print "---"
    except ValueError:
        raise Exception('Not a JSON object: {}'.format(response.text))

def list(args):
    raise Exception('Not implemented yet')

