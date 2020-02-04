import sys
sys.path.append('./')
from elasticsearch import NotFoundError
from helper.transform_format import dictionary_to_array
from config.config_es import INDEX_LAW, TYPE_DOCUMENT
from es_service.es_connection import elasticsearch_connection
from service.search_service.vblp_query_helper import get_source_default, get_sort_by_date_issued, get_sort_by_score, \
    get_filter_scope


def get_by_id(es, id):
    try:
        res = es.get(index=INDEX_LAW, doc_type=TYPE_DOCUMENT, id=id)
        return res['_source']
    except NotFoundError:
        print('not found')
        return {}


def search_content(es, content, match_phrase=False, limit=5, _source=None, editor_setting=None):
    keyword = content
    query = {}
    if _source is None:
        _source = get_source_default()
    if match_phrase:
        query = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match_phrase": {
                                "full_text": keyword
                            }
                        }
                    ]
                }
            },
            # "sort": [get_sort_by_date_issued(), get_sort_by_score()],
            "_source": _source,
            "size": limit
        }
    else:
        query = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "full_text": {
                                    "query": keyword,
                                    # "minimum_should_match": minimum_should_match + '%'
                                }
                            }
                        }
                    ]
                }
            },
            # "sort": [get_sort_by_date_issued(), get_sort_by_score()],
            "_source": _source,
            "size": limit
        }

    filter_builder = []
    if 'scopeId' in editor_setting:
        if editor_setting.get('scopeId') == 1:
            filter_builder.append(get_filter_scope(scope='Toàn quốc'))
    if len(filter_builder) > 0:
        query.get('query').get('bool').update({'filter': filter_builder})

    print(f'querySearchContent: {query}')
    res = es.search(index=INDEX_LAW, doc_type=TYPE_DOCUMENT, body=query)
    print("Got %d Hits:" % res['hits']['total']['value'])
    if res['hits']['total']['value'] == 0:
        return {}
    for hit in res['hits']['hits']:
        print(hit["_source"])
    return res['hits']


def search_title(es, title, limit=5, match_phrase=False, _source=None, editor_setting=None, minimum_should_match="80",
                 filter_builder=None, document_types_condition=None, department_types_condition=None,
                 topic_types_condition=None):
    keyword = title
    query = {}

    if _source is None:
        _source = get_source_default()

    # if match_phrase:
    #     query = {
    #         "query": {
    #             "bool": {
    #                 "should": [
    #
    #                 ],
    #                 "must": [
    #                     {
    #                         "bool": {
    #                             "should": [
    #                                 {
    #                                     "match_phrase": {
    #                                         "Tên VB": keyword
    #                                     }
    #                                 },
    #                                 {
    #                                     "match_phrase": {
    #                                         "Thuộc tính.Thông tin": keyword
    #                                     }
    #                                 }
    #                             ]
    #                         }
    #                     }
    #                 ],
    #                 "must_not": []
    #             }
    #         },
    #         "sort": [get_sort_by_date_issued(), get_sort_by_score()],
    #         "_source": _source,
    #         "size": limit
    #     }
    # else:
    #     query = {
    #         "query": {
    #             "bool": {
    #                 "should": [
    #
    #                 ],
    #                 "must": [
    #                     {
    #                         "bool": {
    #                             "should": [
    #                                 {
    #                                     "match": {
    #                                         "Tên VB": {
    #                                             "query": keyword,
    #                                             "minimum_should_match": minimum_should_match + '%'
    #                                         }
    #                                     }
    #                                 },
    #                                 {
    #                                     "match": {
    #                                         "Thuộc tính.Thông tin": {
    #                                             "query": keyword,
    #                                             "minimum_should_match": minimum_should_match + '%'
    #                                         }
    #                                     }
    #                                 }
    #                             ]
    #                         }
    #                     }
    #                 ],
    #                 "must_not": []
    #             }
    #         },
    #         "sort": [get_sort_by_date_issued(), get_sort_by_score()],
    #         "_source": _source,
    #         "size": limit
    #     }

    query = {
        "query": {
            "match_phrase_prefix": {
                "Tên VB": title
            }
        }
        ,
        "sort": get_sort_by_score(),
        "_source": _source,
        "size": limit
    }

    if document_types_condition is not None:
        must_query = dictionary_to_array(query.get('query').get('bool')['must'])
        new_must_query = must_query + [document_types_condition]
        query.get('query').get('bool').update({'must': new_must_query})

    if department_types_condition is not None:
        must_query = dictionary_to_array(query.get('query').get('bool')['should'])
        new_must_query = must_query + [department_types_condition]
        query.get('query').get('bool').update({'should': new_must_query})

    if topic_types_condition is not None:
        must_query = dictionary_to_array(query.get('query').get('bool')['should'])
        new_must_query = must_query + [department_types_condition]
        query.get('query').get('bool').update({'should': new_must_query})

    if filter_builder is not None and len(filter_builder) > 0:
        query.get('query').get('bool').update({'filter': filter_builder})
    print(f'query: {query}')
    res = es.search(index=INDEX_LAW, doc_type=TYPE_DOCUMENT, body=query)
    print("Got %d Hits:" % res['hits']['total']['value'])
    if res['hits']['total']['value'] == 0:
        return {}
    for hit in res['hits']['hits']:
        # print(hit["_source"])
        pass
    return res['hits']


def search_codes(es, codes, limit=None, _source=None, editor_setting=None):
    query = {}

    if limit is None:
        limit = len(codes)
    if _source is None:
        _source = get_source_default()
    should_query = []
    for code in codes:
        should_query.append(
            {
                "match_phrase": {
                    "Thuộc tính.Số ký hiệu.keyword": code
                }
            }
        )

    query = {
        "query": {
            "bool": {
                "should": should_query
            }
        },
        "sort": [get_sort_by_date_issued(), get_sort_by_score()],
        "_source": _source,
        "size": limit
    }
    res = es.search(index=INDEX_LAW, doc_type=TYPE_DOCUMENT, body=query)
    print("Got %d Hits:" % res['hits']['total']['value'])
    if res['hits']['total']['value'] == 0:
        return {}
    for hit in res['hits']['hits']:
        print(hit["_source"])
    return res['hits']


def example():
    es = elasticsearch_connection
    search_content(es, content="BHXH", match_phrase=False,
                   editor_setting={'documentType': 4, 'title': '', 'departmentIds': [], 'topicIds': [],
                                   'scopeId': 1})
    # search_title(es, title='BHXH', match_phrase=False)
    # get_by_id(es, '75724')
    # get_by_id(es, 'ds')
    # search_codes(es, ['6/2015/NQ-HĐND', '172/2007/NĐ-CP'])

# example()
