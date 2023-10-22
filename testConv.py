import os
import re
import pdfplumber
import copy


def extract_title_abstract(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text_lines(strip=False)

        print(text)

        # for elem in text:
        #     print (elem['text'])

    # return title, abstract


pdf_dir = "./data"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
title_abstract_ist = []

testDir="./data/doc1.pdf"
print(testDir, os.path.join(testDir, testDir) )
extract_title_abstract(testDir)

