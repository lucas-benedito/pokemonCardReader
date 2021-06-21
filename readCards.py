#!/usr/bin/env python3
import json
from collections import Counter
import argparse
from os import putenv

if __name__ == "__main__":
    """Initiate parser"""
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-f', '--file', type=str, help='json file to be processed', required=True,
        default='')
    """Process arguments"""
    params = parser.parse_args()
    fileInput = params.file

if fileInput:
    with open(fileInput) as cardInfo:
      cardInfoJson = json.load(cardInfo)
    n = 0
    cardInfoList = []
    while n<len(cardInfoJson['ObjectStates'][0]['ContainedObjects']):
        if not cardInfoJson['ObjectStates'][0]['ContainedObjects'][n]['Nickname']:
            nickname = 'empty'
        else:
            nickname = cardInfoJson['ObjectStates'][0]['ContainedObjects'][n]['Nickname']
        cardInfoList.append(nickname + ", " + cardInfoJson['ObjectStates'][0]['ContainedObjects'][n]['GUID'])
        n += 1
    cardInfoDict = dict((x,cardInfoList.count(x)) for x in set(cardInfoList))
    with open('OutFile.csv', 'w') as OutFile:
        for key in cardInfoDict:
            quantity = str(cardInfoDict[key])
            value = key +", "+ quantity +"\n"
            OutFile.write(value)