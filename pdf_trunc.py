from pypdf import PdfReader, PdfWriter
from pathlib import Path

'''
This program searches a pdf for query, gets the pages of that pdf and creates a new pdf with the result pages only

Future: integrate this into a class 
'''


def pdf_trunc(query: str, source_path, dest_path):
    hit_pages = []
    source_pdf = Path(source_path)
    dest_pdf = Path(dest_path)
    pdf_read = PdfReader(source_pdf)
    pdf_write = PdfWriter()
    for i in range(0, len(pdf_read.pages)):
        page = pdf_read.pages[i]
        if query in page.extract_text():
            hit_pages.append(page)

    pdf_write.append(fileobj=pdf_read, outline_item='wot_dis', pages=hit_pages)

    with dest_pdf.open(mode='wb') as f:
        pdf_write.write(f)

