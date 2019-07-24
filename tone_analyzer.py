from flask import Flask, jsonify
import json
from os.path import join, dirname
from ibm_watson import ToneAnalyzerV3
from ibm_watson.tone_analyzer_v3 import ToneInput
from task import getHotels
from Hotel import Hotel

app = Flask(__name__)

# If service instance provides API key authentication
service = ToneAnalyzerV3(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    version='2019-07-22',
    iam_apikey='tKXVGSoVxH58no9td0FinudedumIof6MqM2p4IqqJN7N',
    url='https://gateway-lon.watsonplatform.net/tone-analyzer/api')


def getTones():
    listOfHotels = getHotels()
    for hotel in listOfHotels:
        reviewsString = ".".join(hotel.reviews)
        sents = service.tone(
                    tone_input=reviewsString,
                    content_type="text/plain").get_result()
        if "sentences_tone" in sents:
            for sent in sents['sentences_tone']:
                if "tones" in sent:
                    for tone in sent['tones']:
                        if(tone['tone_id']=='joy'):
                            hotel.joyCount = hotel.joyCount+1
                            hotel.joyComm = hotel.joyComm+tone['score']
                        elif(tone['tone_id']=='sadness'):
                            hotel.sadnessCount = hotel.sadnessCount+1
                            hotel.sadnessComm = hotel.sadnessComm+tone['score']
                        elif(tone['tone_id']=='anger'):
                            hotel.angerCount = hotel.angerCount+1
                            hotel.angerComm = hotel.angerComm+tone['score']
        return listOfHotels

def calculateNomalization(listOfHotels):
    for hotel in listOfHotels:
        if(hotel.joyCount>0):
            hotel.joyScore = hotel.joyComm/hotel.joyCount
        if(hotel.sadnessCount>0):
            hotel.sadnessScore = hotel.sadnessComm/hotel.sadnessCount
        if(hotel.angerCount>0):
            hotel.angerScore = hotel.angerComm/hotel.angerCount
    return listOfHotels
    
@app.route('/tones', methods=['GET'])
def get_tasks():
    listOfHotels = getTones()
    listOfHotels = calculateNomalization(listOfHotels)
    jsonResult = jsonify(Hotels=[e.serialize() for e in listOfHotels])
    return jsonResult


if __name__ == '__main__':
    app.run()