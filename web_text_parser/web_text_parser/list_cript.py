# -*- coding: utf-8 -*-
def make_list ():
    # mulher
    with open ("extracted_texts/terra_vida_estilo_mulher.txt", "r") as f:
        urls = f.readlines()
        f.close()
    with open ("extracted_texts/formated_terra_vida_estilo_mulher.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-1] +'\',\n')
        links.write("]")
    # homem
    with open ("extracted_texts/terra_vida_estilo_homem.txt", "r") as f:
        urls = f.readlines()
        f.close()

    with open ("extracted_texts/formated_terra_vida_estilo_homem.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-1] +'\',\n')
        links.write("]")
    # unissex
    with open ("extracted_texts/terra_vida_estilo_unissex.txt", "r") as f:
        urls = f.readlines()
        f.close()

    with open ("extracted_texts/formated_terra_vida_estilo_unissex.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-1] +'\',\n')
        links.write("]")

make_list()
