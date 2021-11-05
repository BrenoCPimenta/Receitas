# How to set up indexes

1. Complete ElasticSearch and Kibana installation, how is described in ../elastic/README.md

2. Run the following command:
```python update_mapping.py -force_reindexation recipes```
    - This command creates a new index named recipes and indexes in the new index the csvs countained in indices/recipes. 
    - Note that the index schemma must be specified in a file called mappings.json. And a empty file called additional_settings.json must exists.