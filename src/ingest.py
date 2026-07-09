import pdfplumber
from pathlib import Path


def extract_text_from_pdf(pdf_path):

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_num, page in enumerate(pdf.pages, start=1):

            text = page.extract_text()

            if text and text.strip():

                pages.append({
                    "page": page_num,
                    "text": text
                })

    return pages


def load_documents(data_dir):

    documents = []

    for pdf in Path(data_dir).glob("*.pdf"):

        pages = extract_text_from_pdf(pdf)

        documents.append({
            "source": pdf.name,
            "pages": pages
        })

    return documents