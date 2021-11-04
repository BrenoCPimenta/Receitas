import argparse
import json
import os

import indexer

from elasticsearch import Elasticsearch

def clone_index(es, index, target):
    try:
        es.indices.put_settings({"index.blocks.write": 'true'}, index=index)
        es.indices.clone(index, target)
        es.indices.put_settings({"index.blocks.write": None}, index=index)
    except:
        print('Não foi possível clonar o índice {}.'.format(index))


def main(args):
    force_reindexation = []
    update_settings = []

    mappings_path = args["mappings_path"]
    elastic_address = args["elastic_address"]
    if args["force_reindexation"] != None:
        force_reindexation = args["force_reindexation"]
    if args["update_settings"] != None:
        update_settings = args["update_settings"]
    for i in update_settings:
        if i in force_reindexation:
            update_settings.remove(i)

    if not os.path.isdir("indices"):
        os.mkdir("indices")
        print("Created new directory: indexer/indices")

    es = Elasticsearch([elastic_address])
    settings = json.load(open('additional_settings.json'))
    updated_mappings = json.load(open(mappings_path))
    local_indices = [index for index in updated_mappings.keys() if es.indices.exists(index)]
    local_mappings = es.indices.get_mapping(local_indices)

    replica_indices = dict([(index, 0) for index in updated_mappings.keys() if 'conteudo' in updated_mappings[index]['mappings']['properties'].keys()])
    
    csv_indexer = indexer.Indexer(elastic_address = elastic_address)
    for index in updated_mappings.keys():
        
        print("Checking " + index + "...")
        
        index_folder = "indices/"+index
        if not os.path.isdir(index_folder):
            os.mkdir(index_folder)
            print("Created new directory: " + index_folder)
        
        # se o indice ja existe e o mapping eh diferente ou se esta na lista de force_reindexation
        if (index in local_indices) and (local_mappings[index] != updated_mappings[index] or index in force_reindexation): 
            es.indices.delete(index)
            print("Existing index deleted: " + index)
            local_indices.remove(index)
            update_settings.append(index)
        
        if index not in local_indices: # caso o indice ainda nao exista ou foi excluido
            es.indices.create(index, body = updated_mappings[index] ) # cria indice
            print("New index created: " + index)
            files_to_index = indexer.list_files(index_folder)
            if len(files_to_index) == 0:
                print("No files to index in " + index_folder)
            else:
                print("Indexing " + str(len(files_to_index)) + " files in " + index)
                csv_indexer.simple_indexer(files_to_index, index) # insere documentos
            # Verifica se é necessário (re)criar uma replica para esse índice
            if index in replica_indices.keys():
                replica = index + '-replica'
                if es.indices.exists(replica):
                    print("Deleting replica of index: " + index)
                    es.indices.delete(replica)
                print("Cloning replica of index: " + index)
                clone_index(es, index, replica)
        
        if index in update_settings:
            if index in settings:
                es.indices.put_settings(index = index, body = settings[index]["settings"]) # atualiza settings
                print("Updated settings from " + index)
            else:
                print("There is no settings to update in " + index)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Verifica se o indice sofreu alguma alteracao e, nesse caso,\
            cria o indice novamente com o dado mapping. Força update dos settings dos dados indices.')
    
    parser.add_argument("-force_reindexation", nargs='+', help="List of indices to force reindexation")
    parser.add_argument("-update_settings", nargs='+', help="List of indices to force settings update")
    parser.add_argument("-mappings_path", default="mappings.json", help="Path of the mappings json file that will be used")
    parser.add_argument("-elastic_address", default="localhost:9200", help="Elasticsearch address. Format: <ip>:<port>")

    # Get all args
    args = vars(parser.parse_args())

    main(args)