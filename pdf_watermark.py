from pypdf import PdfReader, PdfWriter
from pathlib import Path


def watermarker(wm_pages: list, wm_text: str, source_path, dest_path):
    if isinstance(source_path, str):
        source_path = Path(source_path)
    if isinstance(dest_path, str):
        dest_path = Path(dest_path)
    if len(wm_pages) > 1:
        for i, v in enumerate(wm_pages):
            watermarker(wm_pages=v, wm_text=wm_text, source_path=source_path, dest_path=dest_path)
    source_pdf = PdfReader(stream=source_path)
    target_page = source_pdf.pages[wm_pages[0]]
    writer = PdfWriter(clone_from=source_pdf)


reader = PdfReader(stream="Leonar/home/jahn/PycharmProjects/Werd/Leonard Rosenthol - Developing with PDF_ dive into the Portable Document Format (2013, O'Reilly Media) - libgen.li.pdfd")

check = reader.pages[0:1:3]
