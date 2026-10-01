class Document:
    def renderer(self): raise NotImplementedError

class Renderer:
    def render(self, document): raise NotImplementedError

class PdfDocument(Document):
    def renderer(self): return PdfRenderer()

class HtmlDocument(Document):
    def renderer(self): return HtmlRenderer()

class PdfRenderer(Renderer):
    def render(self, document): return "pdf"

class HtmlRenderer(Renderer):
    def render(self, document): return "html"

# Project contract: each new document subtype must have a dedicated renderer subtype.
