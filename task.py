from __future__ import print_function
import numpy as np
import pandas as pd
from Hotel import Hotel


def getHotels():
    dataset = pd.read_csv('../hotel-reviews/7282_1.csv', delimiter = ',')
    hotels = dataset[dataset['categories']=='Hotels']
    hotelsNames = hotels.name.unique()
    listOfHotels = []

    '''
    for i in hotelsNames:
        h = Hotel(i)
        h.reviews = hotels[hotels['name']==i]['reviews.text']
        listOfHotels.append(h)
    '''
    listOfHotels = [Hotel(i , hotels[hotels['name']==i]['reviews.text']) for i in hotelsNames]
    return listOfHotels

#print(listOfHotels[1].name)




'''
print("\ntone_chat() example 1:\n")
utterances = [{
    'text': 'I am very happy.',
    'user': 'glenn'
}, {
    'text': 'It is a good day.',
    'user': 'glenn'
}]

tone_chat = service.tone_chat(utterances).get_result()
print(json.dumps(tone_chat, indent=2))
'''


#listOfHotels = getHotels()
#jsonResult = json.dumps(listOfHotels)
