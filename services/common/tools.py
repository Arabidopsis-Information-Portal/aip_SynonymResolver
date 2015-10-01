NEO4J_SERVER_IP='52.4.211.39'
NEO4J_SERVER_PORT='7474'

def single_transaction_url():
     URL = 'http://' + NEO4J_SERVER_IP + ':' + NEO4J_SERVER_PORT + '/db/data/transaction/commit'
     return URL

def credentials():
    return ('neo4j', '4UbczmDtK4eY6sfS')
