import sys
sys.path.append('./')
from constants.law_constant import DEPARTMENT_TYPES, TOPIC_TYPES
from service.common.common import get_by_attribute_from_array_dict


def get_source_default():
    source = ['url', 'Tên VB', 'Thuộc tính']
    return source


def get_sort_by_date_issued(desc=True):  # Ngày ban hành
    return {
        "Thuộc tính.Ngày ban hành.keyword": {"order": "desc"}
    }


def get_sort_by_score(desc=True):
    return {"_score": {"order": "desc"}}


def get_filter_scope(scope='Toàn quốc'):
    if scope == 'Toàn quốc':
        return {
            "term": {
                "Thuộc tính.Phạm vi.keyword": "Toàn quốc"
            }
        }

    else:
        return None


def get_condition_by_document_type(document_type_name):
    return {
        "match_phrase": {
            "Thuộc tính.Loại văn bản.keyword": {
                "query": document_type_name
            }
        }
    }


def get_condition_by_department_type(department_name):
    return {
        "match_phrase": {
            "Thuộc tính.Ngành.keyword": {
                "query": department_name
            }
        }
    }


def get_condition_by_topic_type(topic_name):
    return {
        "match_phrase": {
            "Thuộc tính.Lĩnh vực.keyword": {
                "query": topic_name
            }
        }
    }


def get_condition_should_by_departments(department_ids):
    department_types_condition_should = []

    for department_id in department_ids:
        department_name = get_by_attribute_from_array_dict(DEPARTMENT_TYPES, 'id', department_id).get(
            'name')
        department_types_condition_should.append(get_condition_by_department_type(department_name))

    department_types_condition = {
        "bool": {
            "should": [
                department_types_condition_should
            ]
        }
    }
    return department_types_condition


def get_condition_should_by_topics(topic_ids):
    topic_types_condition_should = []
    for topic_id in topic_ids:
        topic_name = get_by_attribute_from_array_dict(TOPIC_TYPES, 'id', topic_id).get(
            'name')

        topic_types_condition_should.append(get_condition_by_topic_type(topic_name))

    topic_types_condition = {
        "bool": {
            "should": [
                topic_types_condition_should
            ]
        }
    }
    return topic_types_condition