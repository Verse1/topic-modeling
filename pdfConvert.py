import os
import re
import pdfplumber
import copy


def extract_title_abstract(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]

        text = page.extract_text(x_tolerance=1, y_tolerance=5)

        # print(page.chars)
        table={}
        for x,i in enumerate(page.chars):
            # print(i["text"])
            # if i["text"]==" " or i["text"]=="\n":
            #     print("new line")
            if i["size"] not in table:
                table[i["size"]]=""
            if x>0 and i["x0"]-page.chars[x-1]["x1"]>=1:
                table[i["size"]]+=" "
            if x>0 and page.chars[x-1]["y1"]-i["y1"]>5:
                table[i["size"]]+=" "
            table[i["size"]]+=i["text"]


        # print(text,"\n") 
        tmp=copy.deepcopy(table)

        for i in tmp:
            if len(tmp[i])<30:
                del table[i]

        title=table[max(table.keys())].strip().replace("  "," ")
        abstract_match = re.search(r"Abstract\s+(.*?[.!?])\s*\n[c,©]", text, re.DOTALL)
        if not abstract_match:
            abstract_match = re.search(r'(?i)abstract\b\.?:?]?\s+((?:.|\n)+?)(?=\n\d+\.|Key|Introduction|[0,1]?\Z)', text, re.DOTALL)

        if abstract_match:
            abstract = abstract_match.group(1).strip()

    if not abstract_match:
        abstract = "No abstract found"
    # abstract = text.split('\n')
    # print("Title: ",title,"Abstract: ",abstract)
    # print(title, "\n")

    return title, abstract


pdf_dir = "./data"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
title_abstract_list = []


testDir="./data/doc16.pdf"

print(extract_title_abstract(testDir)[0])

# if title_abstract:
#     title_abstract_list.append(title_abstract)
# title_abstract

# for pdf_file in pdf_files:
#     pdf_path = os.path.join(pdf_dir, pdf_file)
#     print(pdf_file)
#     title_abstract = extract_title_abstract(pdf_path)
#     print("Title",title_abstract[0],"\nAbstract",title_abstract[1])


#     if title_abstract:
#         title_abstract_list.append(title_abstract)
# print(title_abstract_list)
