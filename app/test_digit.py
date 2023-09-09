import pdfplumber

# Open the PDF file
pdf_file_path = r'C:\Users\DELL\incountries_digit_code\All-Country-Codes-List-in-Pdf-Download-for-Free.pdf'

# Create a PDFPlumber object
with pdfplumber.open(pdf_file_path) as pdf:
    # Iterate through each page and extract table data
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        tables = page.extract_tables()

        # Iterate through tables on the page
        for table_num, table in enumerate(tables):
            print(f"Table {table_num + 1}:")
            for row in table:
                print(row)
