import argparse
import json
from elasticsearch import Elasticsearch


def main(args):
    mappings_path = args["mappings_path"]
    elastic_address = args["elastic_address"]
    force_creation = args["force_creation"]

    es = Elasticsearch([elastic_address])
    mappings_json = json.load(open(mappings_path))

    local_indices = [index for index in mappings_json.keys() if es.indices.exists(index)]

    c = 0
    for index_name in mappings_json.keys():
        # se for pra criar o índice de qlqr forma, deleta o antigo caso exista
        if force_creation == True and index_name in local_indices:
            es.indices.delete(index_name)
            local_indices.remove(index_name)
            print('Índice removido:', index_name)
            c += 1
        
        # se o índice não existe, cria ele
        if index_name not in local_indices:
            es.indices.create(index_name, body = mappings_json[index_name])
            local_indices.append(index_name)
            print('Índice criado:', index_name)
            c += 1
    
    if c == 0:
        print('Nenhum índice foi criado ou removido.')



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Cria os índices de acordo com o arquivo de mappings. Irá criar apenas os \
    índices que não existem. Passe -force_creation para recriar mesmo os índices já existentes (isto irá apagar todos os dados).')
    
    parser.add_argument("-force_creation", action='store_true', help="Força a recriação dos índices que já existem")
    parser.add_argument("-mappings_path", default="mappings.json", help="Caminho do arquivo de mappings")
    parser.add_argument("-elastic_address", default="localhost:9200", help="Elasticsearch address. Format: <ip>:<port>")

    # Get all args
    args = vars(parser.parse_args())

    main(args)