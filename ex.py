import requests
import json
import csv

def line_answer(place):
    data={'京都市':3404,'四条':3414,'河原町':3402}
    apikey='0600c456734c0f1315878fc5aeb29fa2&'
    place=data[place]
    url='http://api.gnavi.co.jp/RestSearchAPI/20150630/?keyid={key}&format=json&category_s=RSFST09004&areacode_s=AREAS{place}'.format(key=apikey,place=place)

    html=requests.get(url)

    data=json.loads(html.text)

    with open('restcsvaurant.csv','w',newline='',encoding='utf-8') as w:
        writer=csv.writer(w)
        for k in data['rest']:
            writer.writerow([k['name'],k['url']])

if __name__ == '__main__':
    line_answer()