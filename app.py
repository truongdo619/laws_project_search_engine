from flask import Flask, request, jsonify, send_file
from flask_restplus import Resource, Api, reqparse, inputs
from flask_cors import CORS
from service.search_service.vblp_searcher import search_content, get_by_id, search_title, search_codes, search_match_all
from es_service.es_connection import elasticsearch_connection
from service.search_service.vblp_searcher_for_support import search_for_support
import pdfkit
import json
import ast

def factory():
    app = Flask(__name__, static_url_path='/static')
    app.url_map.strict_slashes = False
    CORS(app)
    return app


app = factory()

api = Api(app, version='1.0', title='Law Tech API',
          description='Law Tech API'
          )

ns = api.namespace('api/lawtech', description='LawTech API')


@ns.route("/document/<string:id>")
class GetById(Resource):
    parser = api.parser()

    @ns.doc('Get document by id', parser=parser)
    def get(self, id):
        print('prepare find', id)
        document = get_by_id(elasticsearch_connection, id)

        return jsonify(document)

match_all_parser = reqparse.RequestParser()
match_all_parser.add_argument('size', type=int, default=5)
match_all_parser.add_argument('from', type=int, default=0)
match_all_parser.add_argument('sorted_by', type=int, default=None)
@ns.route("/document/searchMatchAll")
class searchMatchAll(Resource):

    @ns.expect(match_all_parser)
    def post(self):
        data = match_all_parser.parse_args()
        print(data)
        document = search_match_all(elasticsearch_connection, limit=data['size'], start=data['from'], sort_by=data['sorted_by'])
        return jsonify(document)


content_parse = reqparse.RequestParser()
content_parse.add_argument('content', required=True, default="Bảo hiểm xã hội")
content_parse.add_argument('from', type=int, default=0)
content_parse.add_argument('size', type=int, default=5)
content_parse.add_argument('time_range', default=None, help = 'Example: { "gte" : "1940-01-01", "lte" : "2020-01-01"}')
content_parse.add_argument('match_phrase', type=inputs.boolean, default=False)
content_parse.add_argument('doc_status', default=None)
content_parse.add_argument('document_types_condition', default=None)
content_parse.add_argument('document_field', default=None)
content_parse.add_argument('issuing_body', default=None)
content_parse.add_argument('signer', default=None)
content_parse.add_argument('sorted_by', type=int, default=1)
content_parse.add_argument('editor_setting',  default=None)
@ns.route("/document/searchByContent")
class SearchContent(Resource):

    @ns.expect(content_parse)
    def post(self):
        data = content_parse.parse_args()
        print (data)
        time_range = None
        if data['time_range'] is not None:
            time_range = ast.literal_eval(data['time_range'])
        document = search_content(elasticsearch_connection, content=data['content'], time_range = time_range, match_phrase=data['match_phrase'],
                   limit=data['size'], start=data['from'], doc_status = data['doc_status'], document_types_condition=data['document_types_condition'],
                    document_field=data['document_field'], issuing_body = data['issuing_body'],
                    signer = data['signer'], sorted_by=data['sorted_by'], editor_setting=data['editor_setting'])
        return jsonify(document)
        # return {}

title_parse = reqparse.RequestParser()
title_parse.add_argument('title', required=True, default="Bảo hiểm xã hội")
title_parse.add_argument('from', type=int, default=0)
title_parse.add_argument('size', type=int, default=5)
title_parse.add_argument('time_range', default=None, help = 'Example: { "gte" : "1940-01-01", "lte" : "2020-01-01"}')
title_parse.add_argument('match_phrase', type=inputs.boolean, default=False)
title_parse.add_argument('doc_status', default=None)
title_parse.add_argument('document_types_condition', default=None)
title_parse.add_argument('document_field', default=None)
title_parse.add_argument('issuing_body', default=None)
title_parse.add_argument('signer', default=None)
title_parse.add_argument('sorted_by', type=int, default=1)
title_parse.add_argument('editor_setting',  default=None)
@ns.route("/document/searchByTitle")
class SearchTitle(Resource):

    @ns.expect(title_parse)
    def post(self):
        data = title_parse.parse_args()
        print (data)
        time_range = None
        if data['time_range'] is not None:
            time_range = ast.literal_eval(data['time_range'])
        document = search_title(elasticsearch_connection, title=data['title'], time_range=time_range,
                                  match_phrase=data['match_phrase'],
                                  limit=data['size'], doc_status=data['doc_status'],
                                  start=data['from'],
                                  document_types_condition=data['document_types_condition'],
                                  document_field=data['document_field'],
                                  issuing_body=data['issuing_body'],
                                  signer=data['signer'], sorted_by=data['sorted_by'],
                                  editor_setting=data['editor_setting'])

        return jsonify(document)

code_parse = reqparse.RequestParser()
code_parse.add_argument('code', required=True, default="190/2007/NĐ-CP")
code_parse.add_argument('from', type=int, default=0)
code_parse.add_argument('size', type=int, default=5)
code_parse.add_argument('time_range', default=None, help = 'Example: { "gte" : "1940-01-01", "lte" : "2020-01-01"}')
code_parse.add_argument('match_phrase', type=inputs.boolean, default=False)
code_parse.add_argument('doc_status', default=None)
code_parse.add_argument('document_types_condition', default=None)
code_parse.add_argument('document_field', default=None)
code_parse.add_argument('issuing_body', default=None)
code_parse.add_argument('signer', default=None)
code_parse.add_argument('sorted_by', type=int, default=1)
code_parse.add_argument('editor_setting',  default=None)
@ns.route("/document/searchByCode")
class SearchCodes(Resource):

    @ns.expect(code_parse)
    def post(self):
        data = code_parse.parse_args()
        print (data)
        time_range = None
        if data['time_range'] is not None:
            time_range = ast.literal_eval(data['time_range'])
        document = search_codes(elasticsearch_connection, code=data['code'], time_range=time_range,
                                match_phrase=data['match_phrase'],
                                limit=data['size'], doc_status=data['doc_status'],
                                start=data['from'],
                                document_types_condition=data['document_types_condition'],
                                document_field=data['document_field'],
                                issuing_body=data['issuing_body'],
                                signer=data['signer'], sorted_by=data['sorted_by'],
                                editor_setting=data['editor_setting'])

        return jsonify(document)


# @ns.route("/document/searchForSupport")
# class SearchForSupport(Resource):
#     parser = api.parser()
#
#     parser.add_argument('body', type='json', default="{\r\n\t\"title\": \"Bảo hiểm xã hội\"\r,\"editor_setting\": None}\n}",
#                         required=True,
#                         help='json query', location='json')
#
#     @ns.doc('Search document by title', parser=parser)
#     def post(self):
#         input_form = request.json
#         title = input_form.get('title', '')
#         editor_setting = input_form.get('editor_setting', '')
#         size = min(input_form.get('size', 5), 50)
#         is_match_phrase = input_form.get('is_match_phrase', False)
#         print(input_form, 'content:', title, 'size:', size, 'is_match_phrase:', is_match_phrase)
#         document = search_for_support(elasticsearch_connection, title=title, limit=size,
#                                       is_match_phrase=is_match_phrase,
#                                       editor_setting=editor_setting)
#
#         return jsonify(document)

# @app.route('/api/lawtech/convertToPdf', methods=['GET', 'POST'])
# def convertToPdf():
#     if  request.method == 'POST':
#         print(request.get_json())
#         req_data = request.get_json()
#     print(req_data)
#     options = {
#              'dpi': 365,
#              'page-size': 'A4',
#              'margin-top': '0.25in',
#              'margin-right': '0.25in',
#              'margin-bottom': '0.25in',
#              'margin-left': '0.25in',
#              'encoding': "UTF-8",
#              'custom-header' : [
#                 ('Accept-Encoding', 'gzip')
#              ],
#              'no-outline': None,
#         }
#     pdfkit.from_string(req_data['html'], 'out.pdf', css='example.css', options=options)
#     return send_file('out.pdf', attachment_filename='abc.pdf')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1910, debug=True)
