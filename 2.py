#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
P15040 GEORGE ZERVOLEAS
1/10/2016

THEMA 2
Programma to opoio xrisimopoiei ta web services tou OPAP gia na deiksei statistika gia to KINO ths shmerinhs hmeras mesw syndeshs
sthn selida http://applications.opap.gr/DrawsRestServices/kino/drawDate/HMEROMHNIA.json

"""

import json
import urllib2
from collections import OrderedDict
from datetime import datetime
import sys
from pprint import pprint as pp


def get_distribution(data):
    """
    Fortwsh apotelesmatwn poy epistrefontai 
    Epistrefei: {Arithmos: Syxnothta}
    """
    data = json.loads(data)

    # the distribution dictionary
    dist = {}
    # initialize dist dictionary with 0s
    for i in range(1, 81):
        dist[i] = 0

    draws = data['draws']
    for draw_key in draws:
        for row in draws[draw_key]:
            for result in row['results']:
                dist[result] += 1

    return dist


def reverse_distribution(dist):
    """
    Function to opoio dhmiourgei lista me : Syxnothta : [Arithmos1, Arithmos2,....]
	
    """
    reverse_dist = {}
    for dist_key, dist_value in dist.items():
        # if it's the first time this key is accessed, initialise its value with an empty list
        reverse_dist.setdefault(dist_value, [])
        # append number to list
        reverse_dist[dist_value].append(dist_key)

    return reverse_dist


def stringify_dict_values(dict_):
    """Build and return a string with a beautified representation of the dict values (comma-separated)"""
    values = [str(val) for val in dict_.values()]
    return ', '.join(values)


def main():
    # url gia to JSON Service tou OPAP
    temp_url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/'

    # date = Trexousa Hmeromhnia
    date = datetime.date(datetime.now())
    date_str = date.strftime('%d-%m-%Y')
    url_data = temp_url + date_str + '.json'
  
    web_url = urllib2.urlopen(url_data)
    if web_url.getcode() == 200:
        data = web_url.read()
        dist = get_distribution(data)
    else:
        print('Received Error')

  
    # Elenxoume oti uparxoun klhrwseis shmeraΕλεγχουμε ότι υπάρχουν κληρώσεις σήμερα
    at_least_one_draw = False
    for value in dist.values():
        if value:
            at_least_one_draw = True
    if not at_least_one_draw:
        print('Den vre8hkan apotelesmata. Mhpws den exoun ginei klhrwseis shmera?')
        sys.exit()

    reverse_dist = reverse_distribution(dist)
    reverse_dist = OrderedDict(sorted(reverse_dist.items()))  # Sortaroume ta apotelesmata

   
    least_frequent = OrderedDict([(k, reverse_dist[k]) for k in reverse_dist.keys()[:7]])  # Apo ligotera se Perissotera
    most_frequent = OrderedDict([(k, reverse_dist[k]) for k in reverse_dist.keys()[:-7:-1]])  # Apo perissotera se ligotera

    # Ektupwsh Apotelesmatwn
    print('stoixeia gia thn Trexousa Hmeromhnia: ' + date_str)
    print('***************************************************************')
    print('\nOi 7 ari8moi me th mikroterh emfanish (apo to mikrotero sto megalytero): ')
    print(stringify_dict_values(least_frequent))

    print('\nOi 7 ari8moi me th megalyterh emfanish (apo to megalytero sto mikrotero): ')
    print(stringify_dict_values(most_frequent))


if __name__ == "__main__":
    main()