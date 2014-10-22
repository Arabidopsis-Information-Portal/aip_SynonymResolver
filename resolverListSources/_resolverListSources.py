import json
import requests
import resolver_common

# aip/resolverListSources
#
# Return a list of resolution sources
# Arguments: None
#
# GET api/resolverListKinds to see kinds of identifiers
# Requires headers:
# Accept:application/json
# Content-Type:application/json

'''
{
  "statements" : [ {
    "statement" : "MATCH (a:Identifier { name:'AT4G25530' })-[:SYNONYM_OF*1..2]-(x:Identifier) WHERE NOT x.kind IN ['TAIR', 'NCBI_TaxID'] return DISTINCT x.name, x.kind ORDER BY x.name"
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

# Have we moved to non-JSON queries yet?

def list(arg):

	syn = arg['query']['identifier']
	response = requests.post(
        resolver_common.single_transaction_url(), 
        data=json.dumps({
	        'statements': [{
	                'statement': "MATCH (a:Identifier { name:'%s' })-[:SYNONYM_OF*1..2]-(x:Identifier) WHERE NOT x.kind IN ['TAIR', 'NCBI_TaxID'] return DISTINCT x.name, x.kind ORDER BY x.name" %(syn,) }]}),
	              headers={'Content-Type': 'application/json',
	                       'Accept': 'application/json; charset=UTF-8'})
	                       
# This needs some error handling. What if the remote source doesn't return JSON or times out?	                       
	for result in response.json()['results'][0]['data']:
		print json.dumps({
			'class': 'id_mapping',
			'locus': result['row'][0],
			'type': 'synonym_of',
			'related_entity': syn,
			'direction': 'undirected',
			'related_entity_kind':result['row'][1]}, indent=4)
		print '---'
