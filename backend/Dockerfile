FROM nshou/elasticsearch-kibana

COPY . backend

RUN sudo apt-get update -y
RUN sudo apt-get install -y curl
RUN sudo apt-get install -y python3 python3-pip python3-venv

WORKDIR elasticsearch-7.16.2
RUN echo 'cluster.routing.allocation.disk.threshold_enabled: False' >> ./config/elasticseach.yml
RUN echo 'ingest.geoip.downloader.enabled: false' >> ./config/elasticseach.yml
RUN echo 'xpack.security.enabled: false' >> ./config/elasticseach.yml

WORKDIR ../backend
# RUN sudo python3 -m venv env
# RUN source env/bin/activate
RUN sudo pip3 install -r requirements.txt

# RUN ./wrapper.sh
# WORKDIR database/indexer
# RUN sudo python3 ./update_mapping.py -force_reindexation recipes

# CMD ["ls"]

CMD ./wrapper.sh