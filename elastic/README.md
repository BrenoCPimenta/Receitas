# How to install ElasticSearch and Kibana

1. Download ElasticSearch - version 7.15.1:

    - https://www.elastic.co/pt/downloads/past-releases/elasticsearch-7-15-1


2. Download Kibana - version 7.15.1:

    - https://www.elastic.co/pt/downloads/past-releases/kibana-7-15-1
    3

3. create a new folder insde 'elastic' folder and unzip both files

4. Run ElasticSearch

```./elasticsearch-7.15.1/bin/elasticsearch```

5. When elastic status turn green, run kibana:

```./kibana-7.15.1-linux-x86_64/bin/kibana```

6. Access kibana in http://localhost:5601/ . To manage indexes or make queries, you should access kibana's dev tools: http://localhost:5601/app/dev_tools#/console