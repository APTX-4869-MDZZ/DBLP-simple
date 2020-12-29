from flask import Flask, jsonify
from flask import request

from dbutils import get_papers, get_related_author, get_domain_paper

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
  related_author = get_related_author(author)
  if related_author:
    author_list = related_author.get('related', [])
  else:
    author_list = []
  if len(author_list) > 50:
    author_list = author_list[:50]
  return jsonify(author_list)

@app.route('/dblp/related_domain', methods=['GET'])
def related_domain():
  domain = request.args.get('domain', '')
  query_result = get_domain_paper(domain)
  result = []
  for r in query_result:
    del r['_id']
    result.append(r)
  return jsonify(result)