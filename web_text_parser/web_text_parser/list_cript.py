# -*- coding: utf-8 -*-
def make_list ():
    with open ("extracted_texts/terra_vida_estilo_comportamento_mulher.txt", "r") as f:
        urls = f.readlines()
        f.close()

    with open ("extracted_texts/formated_terra_vida_estilo_comportamento_mulher.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-1] +'\',\n')
        links.write("]")

    with open ("extracted_texts/terra_vida_estilo_comportamento_homem.txt", "r") as f:
        urls = f.readlines()
        f.close()

    with open ("extracted_texts/formated_terra_vida_estilo_comportamento_homem.txt", "w") as links:
        links.write("[ ")
        for l in urls:
            links.write('\''+ l[:len(l)-1] +'\',\n')
        links.write("]")

make_list()
