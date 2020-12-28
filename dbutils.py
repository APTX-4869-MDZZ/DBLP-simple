import re
from pymongo import MongoClient
client = MongoClient('10.176.64.53', 27017)
dblp = client.dblp
infoCol = dblp.info

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

if __name__ == "__main__":
  result = get_papers('multimodal', 'all')
  for r in result:
    print(r)