from fpdf import FPDF
import markdown2
from bs4 import BeautifulSoup

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.add_font("Arial", "", "fonts/arial.ttf", uni=True)
        self.pdf.set_font("Arial", size=12)

    def write_markdown(self, markdown_text):
        # تحويل Markdown إلى HTML
        html = markdown2.markdown(markdown_text)
        soup = BeautifulSoup(html, "html.parser")

        # معالجة العناصر واحدة واحدة
        for element in soup.children:
            if element.name == "h1":
                self.pdf.set_font("Arial", "B", 16)
                self.pdf.multi_cell(0, 10, element.get_text())
                self.pdf.set_font("Arial", size=12)
            elif element.name == "h2":
                self.pdf.set_font("Arial", "B", 14)
                self.pdf.multi_cell(0, 10, element.get_text())
                self.pdf.set_font("Arial", size=12)
            elif element.name == "p":
                self.pdf.multi_cell(0, 10, element.get_text())
            elif element.name == "ul":
                for li in element.find_all("li"):
                    self.pdf.cell(10)  # مسافة بادئة
                    self.pdf.cell(0, 8, f"- {li.get_text()}", ln=True)
            elif element.name == "ol":
                for i, li in enumerate(element.find_all("li"), 1):
                    self.pdf.cell(10)  # مسافة بادئة
                    self.pdf.cell(0, 8, f"{i}. {li.get_text()}", ln=True)
            self.pdf.ln(4)  # مسافة بين العناصر

    def save(self):
        self.pdf.output(self.filename)