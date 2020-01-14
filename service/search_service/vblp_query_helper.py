
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

