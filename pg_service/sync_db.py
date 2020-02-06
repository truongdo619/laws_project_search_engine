import sys
sys.path.append('./')
from pg_service.pg_connection import postgreSQL_pool
from es_service.es_connection import elasticsearch_connection, insert_doc
import ast
from concurrent.futures import ThreadPoolExecutor
from constants.law_constant import ES_MAPPING, PROPERTIES_TERMS, RELATION_TERMS
ps_connection = postgreSQL_pool.getconn()


def extract_properties(id):
    ps_cursor = ps_connection.cursor()
    properties = {}
    records = None
    for key in PROPERTIES_TERMS:
        properties[PROPERTIES_TERMS[key]] = ''
    ps_cursor.execute("select * from laws_extractivedocumentmetadata where extractive_document_id_id = " + str(id))
    tmp = ps_cursor.fetchall()
    if (len(tmp) > 0):
        records = tmp[0]
    if records:
        for row in records:
            properties[PROPERTIES_TERMS[row[4]]] = row[1]
    return properties


def extract_relations(id):
    ps_cursor = ps_connection.cursor()
    relations = {}
    records = None
    for key in RELATION_TERMS:
        relations[RELATION_TERMS[key]] = ''
    ps_cursor.execute("select * from  laws_extractivedocumentschema where source_id_id = " + str(id))
    tmp = ps_cursor.fetchall()

    if (len(tmp) > 0):
        records = tmp[0]
    if records:
        for row in records:
            properties[PROPERTIES_TERMS[row[4]]] = row[1]
    return relations

def index_record(id):

    try:
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute("select * from laws_extractivedocument where id = " + str(id))
        tmp = ps_cursor.fetchall()
        if (len(tmp) > 0):
            doc_record = tmp[0]
        if doc_record:
            law_document = ES_MAPPING
            law_document['id'] = id # Source ID not ID
            if (doc_record[1] is not None and 'N/a' not in law_document.get('Tên VB')):
                law_document['Tên VB'] = doc_record[1]
            if (doc_record[2] is not None and 'N/a' not in law_document.get('full_text')):
                law_document['full_text'] = doc_record[2]
            if (doc_record[7] is not None and 'N/a' not in law_document.get('url')):
                law_document['url'] = doc_record[7]

            law_document['Thuộc tính'] = extract_properties(id)
            law_document['Lược đồ'] = extract_relations(id)

            # index_document_law_to_es(law_document)
    except Exception as e:
        print('error: ', id)

def load_document(doc_ids):
    executor = ThreadPoolExecutor(max_workers=50)
    for id in doc_ids:
        id = id[0]
        executor.submit(index_record, id)

def index_document_law_to_es(law_document):
    es = elasticsearch_connection
    index = "law_tech"
    doc_type = 'document'
    id = law_document.get('id')
    insert_doc(es, index, doc_type, id, law_document, verbose=True)


def execute():

    ps_cursor = ps_connection.cursor()
    ps_cursor.execute("select id from laws_extractivedocument limit 1")
    doc_ids = ps_cursor.fetchall()
    load_document(doc_ids)
    if (postgreSQL_pool):
        postgreSQL_pool.closeall


execute()
