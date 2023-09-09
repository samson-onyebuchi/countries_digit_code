import pdfplumber

def extract_pdf_tables(pdf_file_path):
    try:
        # Attempt to open the PDF file
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
    except FileNotFoundError:
        print(f"Error: The file '{pdf_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the PDF file path
pdf_file_path = r'C:\Users\DELL\instant-deposit-intenship\countries_digit_code\All-Country-Codes-List-in-Pdf-Download-for-Free.pdf'

# Call the function to extract tables from the PDF
extract_pdf_tables(pdf_file_path)
