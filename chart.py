import requests
import os
import json
import datetime

def get_chart(stock, range):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"
    query_string = {"interval":"1d","region":"US","symbol": stock,"lang":"en","range": range}
    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('X_RAPIDAPI_KEY')
    }

    response = requests.request('GET', url, headers=headers, params=query_string)
    response_json = json.loads(response.text)

    y_axis_price = [int(price) for price in response_json['chart']['result'][0]['indicators']['quote'][0]['close']]
    x_axis_time = [datetime.datetime.fromtimestamp(epoch).strftime('%m-%d-%Y')
                   for epoch in response_json['chart']['result'][0]['timestamp']]
    print(y_axis_price)
    print(x_axis_time)


get_chart('aapl', '1mo')

























