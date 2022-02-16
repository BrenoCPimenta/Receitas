#!/bin/bash
../elasticsearch-7.16.2/bin/elasticsearch -E http.host=0.0.0.0 --quiet &

../kibana-7.16.2-linux-x86_64/bin/kibana --allow-root --host 0.0.0.0 -Q &

./wait-elastic.sh