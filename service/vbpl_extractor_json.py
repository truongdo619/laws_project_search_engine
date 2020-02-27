import sys
sys.path.append('./')
import os
from concurrent.futures import ThreadPoolExecutor

from config.config_project import folder_output_path
from helper.reader_helper import load_jsonl_from_gz, load_json
from es_service.es_connection import elasticsearch_connection, insert_doc
from datetime import datetime
import time

def index_record(file, id):
    try:
        law_document = load_json(file)

        law_document.update({'id': str(id)})
        if (law_document['attribute'] is not None):
            try:
                law_document['attribute']['issued_date'] = datetime.strptime(law_document['attribute']['issued_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["issued_date"] = None
            try:
                law_document['attribute']['effective_date'] = datetime.strptime(law_document['attribute']['effective_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["effective_date"] = None
            try:
                law_document['attribute']['expiry_date'] = datetime.strptime(law_document['attribute']['expiry_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["expiry_date"] = None
            try:
                law_document['attribute']['gazette_date'] = datetime.strptime(law_document['attribute']['gazette_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["gazette_date"] = None
            try:
                law_document['attribute']['enforced_date'] = datetime.strptime(law_document['attribute']['enforced_date'], "%d/%m/%Y")
            except:
                law_document['attribute']["enforced_date"] = None

        print(law_document['id'])
        index_document_law_to_es(law_document)
    except Exception as e:
        print("------------------------------------------------------------------------------")
        print('error: ', e)

def get_gz_path(base_path):
    files = []
    for r, d, f in os.walk(base_path):
        for file in f:
            if '.gz' in file:
                files.append(os.path.join(r, file))
    return files


def load_vbpl(raw_path):
    files = get_gz_path(raw_path)
    files = files[224490:]
    executor = ThreadPoolExecutor(max_workers=50)
    for idx, file in enumerate(files):
        executor.submit(index_record, file, idx + 224490)
    #     executor.submit(index_record, file, idx)


def index_document_law_to_es(law_document):
    es = elasticsearch_connection
    index = "law_tech2"
    doc_type = '_doc'
    id = law_document.get('id')
    print(id)
    insert_doc(es, index, doc_type, id, law_document, verbose=True)


def execute():
    raw_path = '/run/media/kodiak/New Volume/20200224_164327/transform'
    load_vbpl(raw_path)

# time.sleep(30)
execute()
