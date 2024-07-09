# Importieren Sie die Module
from markdown import markdown
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Definieren Sie die Dateinamen
input_filename = 'praktikum/README.md'
output_filename_pdf = 'praktikum/readme.pdf'
output_filename_html = 'praktikum/readme.html'

# Öffnen Sie die Eingabedatei und lesen Sie den Inhalt
with open(input_filename, 'r', encoding='utf-8') as f:
    markdown_text = f.read()

# Konvertieren Sie den Markdown-Text in HTML
html_text = markdown(markdown_text, output_format='html4')

# Schreiben Sie den HTML-Text in eine HTML-Datei
with open(output_filename_html, 'w', encoding='utf-8') as f:
    f.write(html_text)

# Konvertieren Sie den HTML-Text in eine PDF-Datei
c = canvas.Canvas(output_filename_pdf, pagesize=letter)
c.drawString(100, 750, html_text)
c.save()
