import pymupdf as fitz # PyMuPDF
 
from io import BytesIO

def extract_text(file_bytes: bytes) -> str:
    doc = fitz.open(stream=BytesIO(file_bytes), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)


# import pdfplumber
# from io import BytesIO

# def extract_text_and_tables(file_bytes: bytes):
#     text = ""
#     tables = []
#     with pdfplumber.open(BytesIO(file_bytes)) as pdf:
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text + "\n"

#             page_tables = page.extract_tables()
#             for table in page_tables:
#                 tables.append(table)
#     return text, tables

# def format_tables(tables):
#     """Format tables as readable plain text"""
#     formatted_tables = []
#     for table in tables:
#         table_str = "\n".join([
#             "\t".join(str(cell) if cell is not None else "" for cell in row)
#             for row in table if row
#         ])
#         formatted_tables.append(table_str)
#     return "\n\n".join(formatted_tables)

