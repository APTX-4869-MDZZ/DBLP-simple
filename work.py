import xml.sax


class DblpHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.author = ""
        self.editor = ""
        self.title = ""
        self.booktitle = ""
        self.pages = ""
        self.year = ""
        self.address = ""
        self.journal = ""
        self.volume = ""
        self.number = ""
        self.month = ""
        self.url = ""
        self.ee = ""
        self.cdrom = ""
        self.cite = ""
        self.publisher = ""
        self.note = ""
        self.crossref = ""
        self.isbn = ""
        self.series = ""
        self.school = ""
        self.chapter = ""
        self.publnr = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        fileds = ['article', 'inproceedings', 'proceedings', 'book',
                  'incollection', 'phdthesis', 'mastersthesis', 'www', 'person', 'data']
        if tag in fileds:
            self.type = tag
            print("type=", self.type)

    def endElement(self, tag):
        if self.CurrentData == "author":
            print('author=', self.author)
        elif self.CurrentData == "editor":
            print('editor=', self.editor)
        elif self.CurrentData == "title":
            print('title=', self.title)
        elif self.CurrentData == "booktitle":
            print('booktitle=', self.booktitle)
        elif self.CurrentData == "pages":
            print('pages=', self.pages)
        elif self.CurrentData == "year":
            print('year=', self.year)
        elif self.CurrentData == "address":
            print('address=', self.address)
        elif self.CurrentData == "journal":
            print('journal=', self.journal)
        elif self.CurrentData == "volume":
            print('volume=', self.volume)
        elif self.CurrentData == "number":
            print('number=', self.number)
        elif self.CurrentData == "month":
            print('month=', self.month)
        elif self.CurrentData == "url":
            print('url=', self.url)
        elif self.CurrentData == "ee":
            print('ee=', self.ee)
        elif self.CurrentData == "cdrom":
            print('cdrom=', self.cdrom)
        elif self.CurrentData == "cite":
            print('cite=', self.cite)
        elif self.CurrentData == "publisher":
            print('publisher=', self.publisher)
        elif self.CurrentData == "note":
            print('note=', self.note)
        elif self.CurrentData == "crossref":
            print('crossref=', self.crossref)
        elif self.CurrentData == "isbn":
            print('isbn=', self.isbn)
        elif self.CurrentData == "series":
            print('series=', self.series)
        elif self.CurrentData == "school":
            print('school=', self.school)
        elif self.CurrentData == "chapter":
            print('chapter=', self.chapter)
        elif self.CurrentData == "publnr":
            print('publnr=', self.publnr)
        self.CurrentData = ""

     # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "editor":
            self.editor = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "booktitle":
            self.booktitle = content
        elif self.CurrentData == "pages":
            self.pages = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "address":
            self.address = content
        elif self.CurrentData == "journal":
            self.journal = content
        elif self.CurrentData == "volume":
            self.volume = content
        elif self.CurrentData == "number":
            self.number = content
        elif self.CurrentData == "month":
            self.month = content
        elif self.CurrentData == "url":
            self.url = content
        elif self.CurrentData == "ee":
            self.ee = content
        elif self.CurrentData == "cdrom":
            self.cdrom = content
        elif self.CurrentData == "cite":
            self.cite = content
        elif self.CurrentData == "publisher":
            self.publisher = content
        elif self.CurrentData == "note":
            self.note = content
        elif self.CurrentData == "crossref":
            self.crossref = content
        elif self.CurrentData == "isbn":
            self.isbn = content
        elif self.CurrentData == "series":
            self.series = content
        elif self.CurrentData == "school":
            self.school = content
        elif self.CurrentData == "chapter":
            self.chapter = content
        elif self.CurrentData == "publnr":
            self.publnr = content


if (__name__ == "__main__"):

    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = DblpHandler()
    parser.setContentHandler(Handler)

    parser.parse("dblp.xml")
