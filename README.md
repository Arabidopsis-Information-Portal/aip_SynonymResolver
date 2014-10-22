Resolver APIs
=============

The included files represent three independent APIs: two search APIs and one list API. The master files for each are resolverListKinds, resolverLookupLocusBySynonym, and resolverLookupSynonymsByLocus. The search APIs expect the parameter "identifier".

```
>>> import resolverLookupLocusBySynonym
>>> resolverLookupLocusBySynonym.search({'identifier': 'FWA'})
{
    "direction": "undirected", 
    "related_entity_kind": "Gene_alias", 
    "locus": "AT4G25530", 
    "related_entity": "FWA", 
    "type": "synonym_of", 
    "class": "id_mapping"
}
```

```
import resolverLookupSynonymsByLocus
>>> resolverLookupSynonymsByLocus.search({'identifier': 'AT4G25530'})
{
    "direction": "undirected", 
    "related_entity_kind": "BioGrid", 
    "locus": "13945", 
    "related_entity": "AT4G25530", 
    "type": "synonym_of", 
    "class": "id_mapping"
}
---
{
    "direction": "undirected", 
    "related_entity_kind": "GI", 
    "locus": "17432948", 
    "related_entity": "AT4G25530", 
    "type": "synonym_of", 
    "class": "id_mapping"
}
...
```

```
import resolverListKinds
>>> resolverListKinds.list({'dummy': 'dictionary'})
{
    "url": "", 
    "class": "identifier_kind", 
    "name": "AT", 
    "id": "AT"
}
---
{
    "url": "", 
    "class": "identifier_kind", 
    "name": "Allergome", 
    "id": "Allergome"
}
---
...
```