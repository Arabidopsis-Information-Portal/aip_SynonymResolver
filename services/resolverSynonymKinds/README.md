resolver_synonym_kinds
======================

The AIP resolver service is aware of many types of database identifiers for AGI loci. This service allows you to list them or search for a specific kind and return just its metadata.

```
curl -sk -L -X GET -H "Authorization: Bearer $TOKEN"  https://api.araport.org/community/v0.3/vaughn-dev/resolver_synonym_kinds_v0.1/list
{"result": [
{"url": "", "id": "AT", "class": "identifier_kind", "name": "AT"}
, {"url": "", "id": "Allergome", "class": "identifier_kind", "name": "Allergome"}
, {"url": "", "id": "BioCyc", "class": "identifier_kind", "name": "BioCyc"}
, {"url": "", "id": "BioGrid", "class": "identifier_kind", "name": "BioGrid"}
, {"url": "", "id": "ChEMBL", "class": "identifier_kind", "name": "ChEMBL"}
, {"url": "", "id": "DIP", "class": "identifier_kind", "name": "DIP"}
, {"url": "", "id": "DNASU", "class": "identifier_kind", "name": "DNASU"}
, {"url": "", "id": "DisProt", "class": "identifier_kind", "name": "DisProt"}
, {"url": "", "id": "DrugBank", "class": "identifier_kind", "name": "DrugBank"}
, {"url": "", "id": "EMBL", "class": "identifier_kind", "name": "EMBL"}
, {"url": "", "id": "EMBL-CDS", "class": "identifier_kind", "name": "EMBL-CDS"}
, {"url": "", "id": "EnsemblGenome", "class": "identifier_kind", "name": "EnsemblGenome"}
, {"url": "", "id": "EnsemblGenome_PRO", "class": "identifier_kind", "name": "EnsemblGenome_PRO"}
, {"url": "", "id": "GI", "class": "identifier_kind", "name": "GI"}
, {"url": "", "id": "GeneFarm", "class": "identifier_kind", "name": "GeneFarm"}
, {"url": "", "id": "GeneID", "class": "identifier_kind", "name": "GeneID"}
, {"url": "", "id": "Gene_alias", "class": "identifier_kind", "name": "Gene_alias"}
, {"url": "", "id": "HOGENOM", "class": "identifier_kind", "name": "HOGENOM"}
, {"url": "", "id": "KEGG", "class": "identifier_kind", "name": "KEGG"}
, {"url": "", "id": "KO", "class": "identifier_kind", "name": "KO"}
, {"url": "", "id": "MEROPS", "class": "identifier_kind", "name": "MEROPS"}
, {"url": "", "id": "MINT", "class": "identifier_kind", "name": "MINT"}
, {"url": "", "id": "NCBI_TaxID", "class": "identifier_kind", "name": "NCBI_TaxID"}
, {"url": "", "id": "OMA", "class": "identifier_kind", "name": "OMA"}
, {"url": "", "id": "PDB", "class": "identifier_kind", "name": "PDB"}
, {"url": "", "id": "PeroxiBase", "class": "identifier_kind", "name": "PeroxiBase"}
, {"url": "", "id": "REBASE", "class": "identifier_kind", "name": "REBASE"}
, {"url": "", "id": "Reactome", "class": "identifier_kind", "name": "Reactome"}
, {"url": "", "id": "RefSeq", "class": "identifier_kind", "name": "RefSeq"}
, {"url": "", "id": "RefSeq_NT", "class": "identifier_kind", "name": "RefSeq_NT"}
, {"url": "", "id": "STRING", "class": "identifier_kind", "name": "STRING"}
, {"url": "", "id": "TAIR", "class": "identifier_kind", "name": "TAIR"}
, {"url": "", "id": "TCDB", "class": "identifier_kind", "name": "TCDB"}
, {"url": "", "id": "UniGene", "class": "identifier_kind", "name": "UniGene"}
, {"url": "", "id": "UniParc", "class": "identifier_kind", "name": "UniParc"}
, {"url": "", "id": "UniPathway", "class": "identifier_kind", "name": "UniPathway"}
, {"url": "", "id": "UniProt", "class": "identifier_kind", "name": "UniProt"}
, {"url": "", "id": "UniProtKB-ID", "class": "identifier_kind", "name": "UniProtKB-ID"}
, {"url": "", "id": "UniRef100", "class": "identifier_kind", "name": "UniRef100"}
, {"url": "", "id": "UniRef50", "class": "identifier_kind", "name": "UniRef50"}
, {"url": "", "id": "UniRef90", "class": "identifier_kind", "name": "UniRef90"}
, {"url": "", "id": "World-2DPAGE", "class": "identifier_kind", "name": "World-2DPAGE"}
, {"url": "", "id": "affy_AG_array_element", "class": "identifier_kind", "name": "affy_AG_array_element"}
, {"url": "", "id": "affy_ATH1_array_element", "class": "identifier_kind", "name": "affy_ATH1_array_element"}
, {"url": "", "id": "eggNOG", "class": "identifier_kind", "name": "eggNOG"}
],
"metadata": {"time_in_main": 2.891362190246582},
"status": "success"}
```