import argparse
from indexer import Indexer, list_files, isfile

parser = argparse.ArgumentParser(description='Indexa arquivos csv no ES dado.')
parser.add_argument("-strategy", choices=['simple', 'parallel'], default="simple", help="Strategy for indexing the data: [simple] or [parallel]")
parser.add_argument("-index", help="Index", required=True)
parser.add_argument("-f", nargs='+', help="List of csv files to index")
parser.add_argument("-d", nargs='+', help="List of directories which all files will be indexed")
parser.add_argument("-t", help="Threadpool size to use for the bulk requests")
parser.add_argument("-elastic_address", default="localhost:9200", help="Elasticsearch address. Format: <ip>:<port>")
args = vars(parser.parse_args()) 

index = args["index"]

files_to_index = []
if args['f'] != None:
    for f in args['f']:
        if isfile(f):
            files_to_index.append(f)
if args['d'] != None:
    for folder in args['d']:
        for f in list_files(folder):
            files_to_index.append(f)

if args["strategy"] == "simple" and args['t'] != None:
    print("WARNING: Argument -t (Threadpool size) is not applicable.")
thread_count = None
if args["strategy"] == "parallel":
    thread_count = 4
    if args['t'] != None:
        thread_count = int(args['t'])

# Index all the csv files in the list
csv_indexer = Indexer(elastic_address=args['elastic_address'])
if args['strategy'] == 'simple':
    csv_indexer.simple_indexer( files_to_index, index)
elif args['strategy'] == 'parallel':
    csv_indexer.parallel_indexer(files_to_index, index, thread_count )