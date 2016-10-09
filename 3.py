#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
P15040 GEORGE ZERVOLEAS
1/10/2016

THEMA 2
Programma to opoio pairnei ws eisodo ena arxeio HOSTS gia Windows kai paragei ena arxeio gia unix:
-xwris Sxolia
-Xwris \r (CR)

"""
import os
import sys

def convert(source_file, dest_file):
    """
    Function h opoia diabazei to Windows Input Arxeio grammi-grammi  xoriw ta sxolia , kai grafei tiw grammes sto output arxeio
    , me antikatastasi tou  \r\n me  \n.

    """
    # Anoigoume to Windows arxeio  gia diabasma
    with open(source_file, 'rb') as source:
        print('Reading content of ' + source_file + '...')
        lines_in = source.readlines()

    print('Converting content to UNIX (ignoring comments)...')
    lines_out = []
    for line in lines_in:
        # afairesh sxolivn
        if line.startswith('#'):
            continue
        # afairesh kenvn
        if line.strip() == '':
            continue
        line = unixify(line)
        lines_out.append(line)

   # Grafoume to apotelesma sto output arxeio
    with open(dest_file, 'wb') as dest:
        print('Writing content to ' + dest_file)
        dest.writelines(lines_out)

def unixify(string_):
    #antikatastasi tou Windows new line me tou Unix
    result = string_.replace('\r\n', '\n')
    return result


if __name__ == '__main__':
   if len(sys.argv) < 3:
    print('Lathos ektelesi - tropos ektelesis: python 3.py HostsWin HostsUnix  ')
    sys.exit()
   file_in = sys.argv[1]
   file_out = sys.argv[2]
   convert(file_in, file_out)
  