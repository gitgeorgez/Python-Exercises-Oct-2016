"""
P15040 GEORGE ZERVOLEAS
1/10/2016

THEMA 4
PROGRAMMA TO OPOIO ALLAZEI pairnei apo ton xristi Onoma tainias kai epistrefei
    a. tin vathmologia
    b. ta braveia
"""
import json
import urllib,urllib2

url = "http://omdbapi.com/?t=" #only submitting the title parameter

movieTitle = raw_input('Dwse tainia: ')
url_data = url + urllib.quote(movieTitle)

web_url = urllib2.urlopen(url_data)
if web_url.getcode() == 200:
     data = web_url.read()
     movies = json.loads(data)
else:
     print('Received Error')
			  
print('Bathmologia Tainias: ' + movies['imdbRating'])
print ('Braveia Tainias: ' + movies['Awards'])
