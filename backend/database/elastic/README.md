# How to install ElasticSearch and Kibana

1. Download ElasticSearch - version 7.15.1:

    - https://www.elastic.co/pt/downloads/past-releases/elasticsearch-7-15-1


2. Download Kibana - version 7.15.1:

    - https://www.elastic.co/pt/downloads/past-releases/kibana-7-15-1


3. Unzip both files in this directory.

4. Run ElasticSearch:

```
./elasticsearch-7.15.1/bin/elasticsearch
```

5. When elastic status turn green or yellow, run kibana:

```
./kibana-7.15.1-linux-x86_64/bin/kibana
```

6. Access kibana in http://localhost:5601/ . To manage indexes or make queries, you should access kibana's dev tools: http://localhost:5601/app/dev_tools#/console 

7. Now, we need to set up some OPTIONAL elasticsearch's configurations. We need to disable some unusefull warnigs and save us some disk space. Add the following lines in the end of "elasticsearch-7.15.1/config/elasticseach.yml":

```
# config/elasticseach.yml
# ...

cluster.routing.allocation.disk.threshold_enabled: False
ingest.geoip.downloader.enabled: false
xpack.security.enabled: false
```

8. Restart elasticseach and kibana with the same commands as above.

9. Follow the instructions on ../indexer/README.md


# How to run elasticseach and kibana

1. Run ElasticSearch

```
./elasticsearch-7.15.1/bin/elasticsearch
```

2. When elastic status turn green or yellow, run kibana:

```
./kibana-7.15.1-linux-x86_64/bin/kibana
```


# Problemas encontrados

1. O ElasticSearch janta memoria, então se vc tiver pouca memoria ou não quiser dividir sua ram com esse fominha, vc pd limitar a quantidade de memoria usada por ele, para isso, crie um arquivo chamado memory.options dentro do diretorio ```elasticsearch-7.15.1/config/jvm.options.d/``` , esse arquivo deve ter a seguinte conteudo (caso 1g ainda seja muito tente frações, por ex 500m):

```
-Xms1g
-Xmx1g
```