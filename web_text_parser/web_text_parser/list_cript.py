# -*- coding: utf-8 -*-
def make_list ():
    with open ("extracted_texts/links_folhasp_michel_temer.txt", "r") as f:
        urls = f.readlines()
        f.close()

    with open ("extracted_texts/list_links_michel_folha.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-2] +'\',\n')
        links.write("]")

make_list()
