import json
import requests
import re
import resolver_common

# aip/resolverLookupSynonymsByLocus
#
# Given any known AGI locus, return the list of known synonyms
# Arguments
# query - STRING (mandatory)

# Sending the following package to neo4j REST API single transaction endpoint
# If we were doing a batch type query, we'd want to leave the transaction open
# 
# POST http://host:7474/db/data/transaction/commit
# Requires headers:
# Accept:application/json
# Content-Type:application/json

def search(arg):

# arg contains a dict with one key:value
#
# locus is gene identifier

	# In the future, ADAMA will check a query, map_*, or generic request against a list of mandatory
	# parameters specified for each service. For now, if we want to enforce that behavior we need to 
	# implement it ourselves. 
    if not ('locus' in arg):
        #print "Locus was not specified"
        return

    term = arg['locus']
    term = term.upper()
    # Ensure term is a valid AGI locus
    p = re.compile('AT[1-5MC]G[0-9]{5,5}', re.IGNORECASE)
    if not p.search(term):
        #print "Invalid AGI locus identifier"
        return

    payload = json.dumps({'statements': [{
'statement': "MATCH (a:Identifier { name:'%s' })-[:SYNONYM_OF*1..2]-(x:Identifier) WHERE NOT x.kind IN ['TAIR', 'NCBI_TaxID'] return DISTINCT x.name, x.kind ORDER BY x.name" %(term,) }]})
    response = requests.post(resolver_common.single_transaction_url(), data=payload, headers={'Content-Type': 'application/json','Accept': 'application/json; charset=UTF-8'})
    
    if response.ok:
        for result in response.json()['results'][0]['data']:
            print json.dumps({
			'class': 'locus_id_mapping',
			'related_entity': result['row'][0],
			'locus': term,
			'relationships': [{'type': 'synonymous_with', 'direction': 'undirected', 'scores': [{'confidence': 1.00 }] }],
			'related_entity_kind':result['row'][1]})
            print "---"
    else:
        return

def list(arg):
    # Unimplemented list method
    pass
    
def help(arg):
    # Placeholder for inline help presented in Markdown or other format
    pass
