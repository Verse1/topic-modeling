import os
import re
import pdfplumber


def extract_title_abstract(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text(x_tolerance=1, y_tolerance=5)
        # print(text)

        abstract_match = re.search(r"Abstract\s+(.*?[.!?])\s*\n[c,©]", text, re.DOTALL)
        if not abstract_match:
            abstract_match = re.search(r'(?i)abstract\b\.?:?]?\s+((?:.|\n)+?)(?=\n\d+\.|Key|Introduction|[0,1]?\Z)', text, re.DOTALL)

        if abstract_match:
            abstract = abstract_match.group(1).strip()

    title = "".join(text.split("\n")[2:4])
    if not abstract_match:
        abstract = "No abstract found"
    # abstract = text.split('\n')
    # print("Title: ",title,"Abstract: ",abstract)
    print(abstract, "\n")

    # return title, abstract


pdf_dir = "./data"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
title_abstract_list = []

testDir="./data/doc21.pdf"
print(testDir, os.path.join(testDir, testDir) )
extract_title_abstract(testDir)


# if title_abstract:
#     title_abstract_list.append(title_abstract)
# title_abstract

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    print(pdf_file)
    title_abstract = extract_title_abstract(pdf_path)


    # if title_abstract:
    #     title_abstract_list.append(title_abstract)
