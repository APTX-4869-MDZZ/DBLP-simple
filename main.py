from flask import Flask, jsonify
from flask import request

from dbutils import get_papers

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