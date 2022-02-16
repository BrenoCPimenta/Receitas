#!/bin/bash
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9200  )
echo "Waiting for elasticsearch..."
while [ $response != "200" ]
do
    sleep 5;
    response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9200  )
done

echo "Elastic search started"

cd database/indexer
sudo python3 update_mapping.py -force_reindexation recipes

cd ../../api
echo "Starting backend"
python3 manage.py runserver 0.0.0.0:${PORT}