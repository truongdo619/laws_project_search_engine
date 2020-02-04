from flask import Flask, request, jsonify, send_file
from flask_restplus import Resource, Api
from flask_cors import CORS
from service.search_service.vblp_searcher import search_content, get_by_id, search_title, search_codes
from es_service.es_connection import elasticsearch_connection
from service.search_service.vblp_searcher_for_support import search_for_support
import pdfkit

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


@ns.route("/document/searchByContent")
class SearchContent(Resource):
    parser = api.parser()

    parser.add_argument('body', type='json',
                        default="{\r\n\t\"content\": \"Bảo hiểm xã hội\"\r,\"editor_setting\":{}}\n", required=True,
                        help='json query', location='json')

    def post(self):
        input_form = request.json
        content = input_form.get('content', '')
        editor_setting = input_form.get('editor_setting', '')
        size = min(input_form.get('size', 5), 50)
        is_match_phrase = input_form.get('is_match_phrase', False)
        print(input_form, 'content:', content, 'size:', size, 'is_match_phrase:', is_match_phrase)
        document = search_content(elasticsearch_connection, content=content, limit=size, match_phrase=is_match_phrase,editor_setting=editor_setting)
        return jsonify(document)
        # return {}

@ns.route("/document/searchByTitle")
class SearchTitle(Resource):
    parser = api.parser()

    parser.add_argument('body', type='json', default="{\r\n\t\"title\": \"Bảo hiểm xã hội\"\r,\"editor_setting\":{}\n}",
                        required=True,
                        help='json query', location='json')

    @ns.doc('Search document by title', parser=parser)
    def post(self):
        input_form = request.json
        content = input_form.get('title', '')
        editor_setting = input_form.get('editor_setting', '')
        size = min(input_form.get('size', 5), 50)
        is_match_phrase = input_form.get('is_match_phrase', False)
        print(input_form, 'content:', content, 'size:', size, 'is_match_phrase:', is_match_phrase)
        document = search_title(elasticsearch_connection, title=content, limit=size, match_phrase=is_match_phrase,
                                editor_setting=editor_setting)

        return jsonify(document)


@ns.route("/document/searchForSupport")
class SearchForSupport(Resource):
    parser = api.parser()

    parser.add_argument('body', type='json', default="{\r\n\t\"title\": \"Bảo hiểm xã hội\"\r,\"editor_setting\":{}\n}",
                        required=True,
                        help='json query', location='json')

    @ns.doc('Search document by title', parser=parser)
    def post(self):
        input_form = request.json
        title = input_form.get('title', '')
        editor_setting = input_form.get('editor_setting', '')
        size = min(input_form.get('size', 5), 50)
        is_match_phrase = input_form.get('is_match_phrase', False)
        print(input_form, 'content:', title, 'size:', size, 'is_match_phrase:', is_match_phrase)
        document = search_for_support(elasticsearch_connection, title=title, limit=size,
                                      is_match_phrase=is_match_phrase,
                                      editor_setting=editor_setting)

        return jsonify(document)


@ns.route("/document/searchByCodes")
class SearchCodes(Resource):
    parser = api.parser()

    parser.add_argument('body', type='json', default="{\r\n\t\"codes\": \"[]\"\r,\"editor_setting\":{}\n}",
                        required=True,
                        help='json query', location='json')

    @ns.doc('Search document by codes', parser=parser)
    def post(self):
        input_form = request.json
        codes = input_form.get('codes', [])
        editor_setting = input_form.get('editor_setting', '')
        size = min(input_form.get('size', len(codes)), 50)
        print(input_form, 'codes:', codes, 'size:', size)
        document = search_codes(elasticsearch_connection, codes=codes, limit=size, editor_setting=editor_setting)

        return jsonify(document)


@app.route('/api/lawtech/convertToPdf', methods=['GET', 'POST'])
def convertToPdf():
    if  request.method == 'POST':
        print(request.get_json())
        req_data = request.get_json()
    print(req_data)
    options = {
             'dpi': 365,
             'page-size': 'A4',
             'margin-top': '0.25in',
             'margin-right': '0.25in',
             'margin-bottom': '0.25in',
             'margin-left': '0.25in',
             'encoding': "UTF-8",
             'custom-header' : [
                ('Accept-Encoding', 'gzip')
             ],
             'no-outline': None,
        }
    pdfkit.from_string(req_data['html'], 'out.pdf', css='example.css', options=options)
    return send_file('out.pdf', attachment_filename='abc.pdf')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1910, debug=True)
