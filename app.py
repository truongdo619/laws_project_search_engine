from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_cors import CORS
from service.search_service.vblp_searcher import search_content, get_by_id
from es_service.es_connection import elasticsearch_connection

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

    def post(self):
        input_form = request.json
        content = input_form.get('content', '')
        size = min(input_form.get('size', 5), 50)
        is_match_phrase = input_form.get('is_match_phrase', False)
        print(input_form, 'content:', content, 'size:', size, 'is_match_phrase:', is_match_phrase)
        document = search_content(elasticsearch_connection, content=content, limit=size, match_phrase=is_match_phrase)
        return jsonify(document)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1910, debug=True)