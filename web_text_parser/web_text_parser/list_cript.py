# -*- coding: utf-8 -*-
def make_list ():
    with open ("extracted_texts/links_folhasp_michel_temer_31-08-2017--31-08-2018.txt", "r") as f:
        urls = f.readlines()
        f.close()

    with open ("extracted_texts/list_links_folhasp_michel_temer_31-08-2017--31-08-2018.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-1] +'\',\n')
        links.write("]")

make_list()
