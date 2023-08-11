from pypdf import PdfReader

'''

class expansion
pscanner class
init(pdf_path)
results = psearch(query)
results.p_out *prints

could also integrate with file search so 
that program scans through all the pdf documents in 
a folder
'''


def pdf_search(query: str, pdf_path):
    hit_contents = []
    hit_page_nums = []

    pdf = PdfReader(pdf_path)
    for i in range(0, len(pdf.pages)):
        page = pdf.pages[i]
        if query in page.extract_text():
            hit_contents.append(page.extract_text())
            hit_page_nums.append(i)

    for i, v in enumerate(hit_contents):
        print('\n')
        print(f"--------{hit_page_nums[i]}----------")
        print(v)

# how do i multipage
# print(page.extract_text())
