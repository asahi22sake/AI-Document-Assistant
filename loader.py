from pypdf import PdfReader


def extract_pdf_text(uploaded_files):
    """
    Extract text from one or more uploaded PDF files.
    """

    text = ""

    for pdf in uploaded_files:

        reader = PdfReader(pdf)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text