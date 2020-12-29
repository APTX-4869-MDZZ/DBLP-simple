import re
from pymongo import MongoClient
client = MongoClient('10.176.64.53', 27017)
dblp = client.dblp
infoCol = dblp.info
authorCol = dblp.author

def get_papers(keyword, field):
  keyword_regex = re.compile(keyword)
  fields = ['type', 'author', 'editor', 'title', 'booktitle', 'pages', 'year', 'address', 'journal', 'volume', 'number', 'month', 'url', 'ee', 'cdrom', 'cite', 'publisher', 'note', 'crossref ', 'isbn', 'series', 'school', 'chapter', 'publnr']
  query_dict = {}
  if field == 'all':
    query_dict['$or'] = []
    for field in fields:
      query_dict['$or'].append({field: keyword_regex})
  else:
    query_dict[field] = keyword_regex
  result = infoCol.find(query_dict).limit(50)
  return result

def create_related_author():
  author_dict = dict()
  for paper in infoCol.find({}, {'author': 1}):
    if paper.get('author', None):
      authors = paper['author'].split(',')
      author_set = set(authors)
      for author in authors:
        author_set.remove(author)
        author_dict[author] = author_dict.get(author, set()) | author_set
        author_set.add(author)
  for author in author_dict.keys():
    authorCol.insert({
      'name': author,
      'related': list(author_dict.get(author, []))
    })

def get_related_author(name):
  return authorCol.find_one({'name': name})

def get_domain_paper(domain):
  return infoCol.find({'domain': domain}).limit(50)

if __name__ == "__main__":
  for r in get_domain_paper('Natural language processing'):
    print(r)