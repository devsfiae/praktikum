# Importieren Sie die Module
from markdown import markdown
from fpdf import FPDF

# Erstellen Sie eine PDF-Klasse
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Header', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Seite {self.page_no()}', 0, 0, 'C')

# Erstellen Sie eine PDF-Instanz
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Öffnen Sie die Eingabedatei und lesen Sie den Inhalt
input_filename = 'praktikum/README.md'
with open(input_filename, 'r', encoding='utf-8') as f:
    markdown_text = f.read()

# Schreiben Sie den Markdown-Text direkt in die PDF-Datei
pdf.multi_cell(0, 10, markdown_text.encode('latin-1', 'replace').decode('latin-1'))
pdf.output('praktikum/readme.pdf')
