
import sys
sys.path.append('./')
import ast
from concurrent.futures import ThreadPoolExecutor

from config.config_project import folder_output_path
from helper.reader_helper import get_content, is_exist_file
from es_service.es_connection import elasticsearch_connection, insert_doc

import pandas as pd


def index_record(raw_path, law_document):
    try:
        id = law_document.get('url').split('ItemID=')[1].split('&')[0]
        law_document.update({'id': id})
        full_text = ''
        full_text_eng = ''
        if (law_document.get('Toàn văn') is not None and 'N/a' not in law_document.get('Toàn văn')):
            full_text_file_path = raw_path + '/data/' + law_document.get('Toàn văn')
            if (is_exist_file(full_text_file_path)):
                full_text = get_content(full_text_file_path)
                # print(full_text_file_path)
                # break
            else:
                # pass
                print(full_text_file_path + ' is not exist')

        if (law_document.get('VB Tiếng anh') is not None and 'N/a' not in law_document.get('VB Tiếng anh')):
            full_text_eng_file_path = raw_path + '/data/' + law_document.get('VB Tiếng anh')
            if (is_exist_file(full_text_eng_file_path)):
                full_text_eng = get_content(full_text_eng_file_path)
                # print(full_text_eng_file_path )
                # break
            else:
                # pass
                print(full_text_eng_file_path + ' is not exist')

        # print(row_dict)
        if (law_document['Thuộc tính'] is not None and 'N/a' not in law_document['Thuộc tính']):
            law_document['Thuộc tính'] = ast.literal_eval(law_document['Thuộc tính'])

        if (law_document['Lịch sử'] is not None and 'N/a' not in law_document['Lịch sử']):
            law_document['Lịch sử'] = ast.literal_eval(law_document['Lịch sử'])

        if (law_document['VB Liên Quan'] is not None and 'N/a' not in law_document['VB Liên Quan']):
            law_document['VB Liên Quan'] = ast.literal_eval(law_document['VB Liên Quan'])

        if (law_document['Lược đồ'] is not None and 'N/a' not in law_document['Lược đồ']):
            law_document['Lược đồ'] = ast.literal_eval(law_document['Lược đồ'])
        law_document['full_text'] = full_text
        law_document['full_text_eng'] = full_text_eng
        # print(row_dict)
        # print(row['url'])
        # print(row['Tên VB'])
        # print(row['Toàn văn'])
        # print(row['VB Tiếng anh'])
        # print(row['Thuộc tính'])
        # print(row['Lịch sử'])
        # print(row['VB Liên Quan'])
        # print(row['Lược đồ'])
        # break
        index_document_law_to_es(law_document)
    except Exception as e:
        # print(e)
        print('error: ', law_document)


def load_vbpl_csv(raw_path):
    df = pd.read_csv(raw_path + '/data.csv')
    executor = ThreadPoolExecutor(max_workers=50)

    for idx, row in df.iterrows():
        law_document = row.to_dict()
        # index_record(raw_path, law_document)
        executor.submit(index_record, raw_path, law_document)


def index_document_law_to_es(law_document):
    es = elasticsearch_connection
    index = "law_tech"
    doc_type = 'document'
    id = law_document.get('id')
    print(id)
    insert_doc(es, index, doc_type, id, law_document, verbose=True)


def execute():
    raw_path = folder_output_path + '/vbpl/raw'
    load_vbpl_csv(raw_path)


execute()
