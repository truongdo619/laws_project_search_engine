
import sys
sys.path.append('./')
from config.config_project import ES_IP, ES_USER, ES_PASS, ES_PORT

from es_service.es_helper import check_status_es
from datetime import datetime

from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch import helpers

elasticsearch_connection = Elasticsearch(
    ['http://' + ES_USER + ':' + ES_PASS + '@' + ES_IP + ':' + ES_PORT ],
    verify_certs=False, timeout=30)


def insert_doc(es, index, doc_type, id, body, verbose=True):
    res = es.index(index=index, doc_type=doc_type, id=id, body=body)
    es.indices.refresh(index=index)
    if verbose:
        print(res)
    return True


def insert_docs_in_bulk(es, index, doc_type, data_bulk, id_fields='_id', verbose=True):
    actions = []

    for doc in data_bulk:
        _id = doc.get(id_fields)
        if (_id is None):
            continue
        # doc.pop(id_fields)  # remove _id in body

        action = {
            "_index": index,
            "_type": doc_type,
            "_id": _id,
            "_source": doc
        }

        actions.append(action)
    print('prepare insert bulk')
    print(actions)
    res = helpers.bulk(es, actions, raise_on_error=True)
    if verbose:
        print(res)

    return res


def remove_doc(es, index, doc_type, id, verbose=True):
    try:
        output = es.delete(index=index, doc_type=doc_type, id=id)
    except NotFoundError as e:
        print('id %s not found' % id)
        return False
    if verbose:
        print(output)
    return True


def remove_all_doc_from_index(es, index, verbose=True):
    res = es.indices.delete(index=index)
    if verbose: print(res)
    return True


def search(es, query={"query": {"match_all": {}}}):
    res = es.search(index="test-index", body=query)
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


def example():
    es = elasticsearch_connection
    check_status_es(es)
    # index = "test-index"
    # doc_type = 'tweet'
    # body = {
    #     'author': 'tuantm',
    #     'text': 'Elasticsearch: cool. bonsai cool.',
    #     'timestamp': datetime.now(),
    # }
    # id = 2

    # insert_doc(es, index, doc_type, id, body, verbose=True)
    # remove_doc(es, index, doc_type, 2)

    # data_bulk = [
    #     {
    #         '_id': 1,
    #         'title': 'hihi',
    #         'url': 'this is a url'
    #     },
    #     {
    #         '_id': 2,
    #         'title': 'hihi',
    #         'url': 'this is a url'
    #     },
    #     {
    #         '_id': 3,
    #         'title': 'hihi',
    #         'url': 'this is a url'
    #     }
    # ]
    # insert_docs_in_bulk(es, index, doc_type, data_bulk, '_id')
    # remove_all_doc_from_index(es, index)
    # print('done')

# example()
