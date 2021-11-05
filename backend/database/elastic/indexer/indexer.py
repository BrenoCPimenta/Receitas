import csv
import ctypes
import os
import time
import json
from random import random
import datetime

import nltk
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from nltk import tokenize
nltk.download('punkt')

from os import listdir
from os.path import isfile, join


def list_files(path):
    """
    List all files from a given folder
    """
    if path[-1] != "/":
        path = path+"/"
    return [path+f for f in listdir(path) if isfile(join(path, f))]


def get_sentences(text):
    tokens = text.replace("\n", "").replace("\r", "").split()
    text = " ".join(tokens)
    return tokenize.sent_tokenize(text)


def get_dense_vector(text):
    return [random() for i in range(768)]


def parse_date(text):
    for fmt in ('%Y-%m-%d', "%d-%m-%Y"):
        try:
            return datetime.datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')

class Indexer:

    def __init__(self, elastic_address='localhost:9200'):

        self.ELASTIC_ADDRESS = elastic_address
        self.es = Elasticsearch([self.ELASTIC_ADDRESS], timeout=120, max_retries=3, retry_on_timeout=True)

        csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))

    def generate_formated_csv_lines(self, file_path, index, encoding="utf8"):
        """
        Generates formated entries to indexed by the bulk API
        """
        file = open(file_path, encoding=encoding)
        table = csv.DictReader(file)
        columns = table.fieldnames.copy()

        for line in table:
            line = dict(line)
            doc = {}
            for field in columns:
                if line[field] == '':
                    continue

                field_name = field
                field_type = None
                if len(field.split(":")) > 1:
                    field_name = field.split(":")[0]
                    field_type = field.split(":")[-1]

                if field_type == "list":
                    doc[field_name] = eval(line[field])
                elif field_name == 'data':
                    if line[field] != '':
                        element = parse_date(line[field])
                        timestamp = datetime.datetime.timestamp(element)
                        doc[field_name] = timestamp
                else:
                    doc[field_name] = line[field]

            # sentences = get_sentences(line['conteudo'])
            # doc["sentences_vectors"] = [{"vector": get_dense_vector(sent)} for sent in sentences]
            doc["sentences_vectors"] = []

            yield {
                "_index": index,
                "_source": doc
            }

    def simple_indexer(self, files_to_index, index):
        """
        Index the csvs files using helpers.bulk
        """
        start = time.time()

        responses = {}
        for csv_file in files_to_index:
            print("Indexing: " + csv_file)
            responses[csv_file] =  helpers.bulk(self.es, self.generate_formated_csv_lines(csv_file, index) )
            print("  Response: " + str(responses[csv_file]))

            if len(responses[csv_file][1]) > 0 :
                print("Detected error while indexing: " + csv_file)
            else:
                end = time.time()
                print("Indexing time: {:.4f} seconds.".format(end-start))

    def parallel_indexer(self, files_to_index, index, thread_count):
        """
        Index the csvs files using helpers.parallel_bulk
        Note that the queue_size is the same as thread_count
        """
        start = time.time()

        error = False
        for csv_file in files_to_index:
            try:
                print("Indexing: " + csv_file + "...")
                for success, info in helpers.parallel_bulk(self.es, self.generate_formated_csv_lines(csv_file, index), thread_count = thread_count, queue_size = thread_count): 
                    if not success:
                        print("Detected error while indexing: " + csv_file)
                        error = True
                        print(info)
            except:
                error = True
                print("Detected error while indexing: " + csv_file)

        if not error:
            print("All files indexed with no error.")
            end = time.time()
            print("Indexing time: {:.4f} seconds.".format(end-start))
        else:
            print("Error while indexing.")