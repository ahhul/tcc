# -*- coding: utf-8 -*-
import re

def load_text (text_path):
    with open (text_path, 'r') as f:
        lines = f.readlines ()
        for l in lines:
            l.strip ()
    return lines

def clean_break_line (text_lines):
    re_break = re.compile (r'\\n')
    clean_text = []
    for l in text_lines:
        new_line = l.strip()
        re.sub(re_break, "", new_line)
        
        if new_line != '':
            clean_text.append(new_line)
        
    return clean_text

#print (clean_break_line(load_text ('../web_text_parser/web_text_parser/extracted_texts/folhasp/dilma_folha/text_1508558-a-derrota-de-dilma.txt')))

