#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
P15040 GEORGE ZERVOLEAS
23/9/2016

THEMA 6
PROGRAMMA TO OPOIO ALLAZEI MONO TIS LEXEIS MIAS PROTASHS, KAI SYGKEKEIRMENA
    a. to proto gramma paei sto telos
    b. sto telos prostithetai h katalhksh: 'argh'
"""
import re


def main():
    suffix = 'argh'

    input_sentence = raw_input('Dwse protasi: ')

    # Gia ellhnikous Xarakthres
    input_sentence = input_sentence.decode('utf-8')

    new_sentence = transform_sentence(input_sentence, suffix)

    print('Nea protasi: \n' + new_sentence)


def transform_sentence(input_sentence, suffix):
    tokens = re.findall(r"\w+|[^\w]", input_sentence, re.UNICODE)  # list
   
    # Allagh mono twn leksewn
    transformed_tokens = []
    for token in tokens:
        if token.isalpha():
            transformed_token = transform_token(token, suffix)
            transformed_tokens.append(transformed_token)
        else:
            transformed_tokens.append(token)

	# Kataskeyh telikhs protasis
    new_sentence = "".join(transformed_tokens)

    return new_sentence


def transform_token(token, suffix):
    return token[1:] + token[0] + suffix


if __name__ == '__main__':
    main()
	