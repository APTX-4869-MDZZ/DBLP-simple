from flask import Flask, jsonify
from flask import request

from dbutils import get_papers, get_related_author

app = Flask(__name__)

@app.route('/dblp/search', methods=['GET'])
def search():
  query = request.args.get('q', '')
  field = request.args.get('field', 'title')
  query_result = get_papers(query, field)
  result = []
  for r in query_result:
    del r['_id']
    result.append(r)
  return jsonify(result)

@app.route('/dblp/related_author', methods=['GET'])
def related_author():
  author = request.args.get('author', '')
  related_author = get_related_author(author).get('related', [])
  return jsonify(related_author)