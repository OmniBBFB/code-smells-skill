class Document:
    def __init__(self, body): self.body = body

class PdfDocument(Document): pass
class HtmlDocument(Document): pass

class Renderer:
    def render(self, document): return document.body

class ScreenRenderer(Renderer): pass
class PrintRenderer(Renderer): pass

# Output media and document variants are independent; all combinations are allowed.
