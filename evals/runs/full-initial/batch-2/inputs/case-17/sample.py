class Document: pass
class PdfDocument(Document): pass
class HtmlDocument(Document): pass
class Renderer: pass
class PdfRenderer(Renderer): pass
class HtmlRenderer(Renderer): pass
# Factories, registry and extension contract are not supplied.
