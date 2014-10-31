import json
import requests
import re
import resolver_common

# aip/resolverLookupLocusBySynonym
#
# Given any (known) name for a locus, resolve the name to that locus
# Arguments
# query - STRING (mandatory)
#
# Sending the following package to neo4j REST API single transaction endpoint
# If we were doing a batch type query, we'd want to leave the transaction open
#
# POST http://localhost:7474/db/data/transaction/commit
# Requires headers:
# Accept:application/json
# Content-Type:application/json


# Future work: Refactor this to use a cascade of approaches
# and to fail gracefully if we can't figure it out
# For the Interaction viewer, if it is returning intact: namespace this means it can't resolve to anything
# Search order: UniProt resolver; maybe EBI PICR (http://www.ebi.ac.uk/Tools/picr/RESTDocumentation.do); Local

def search(arg):

# arg contains a dict with one key:value
#
# syn is the synonym

    if not ('identifier' in arg):
        #print "The identifier parameter was not specified"
        return

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

    response = requests.post( resolver_common.single_transaction_url(),data=payload, headers={'Content-Type': 'application/json','Accept': 'application/json; charset=UTF-8'})

    # This needs some error handling.
    # What if the remote source doesn't return JSON or times out?
    if response.ok:
        for result in response.json()['results'][0]['data']:
            print json.dumps({
            'class': 'locus_id_mapping',
            'locus': result['row'][0],
            'relationships': [{'type': 'synonymous_with', 'direction': 'undirected', 'scores': [{'confidence': 1.00 }]}],
            'related_entity': syn,
            'related_entity_kind':result['row'][1]})
            print '---'
    else:
        return
    


def resolve_uniprot(arg1):
    # Future code to directly use the Uniprot service for resolution
    pass

def list(arg):
    # Unimplemented list method
    pass

def help(arg):
    # Placeholder for inline help presented in Markdown or other format
    pass