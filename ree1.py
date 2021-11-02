import requests
import json
import pandas as pd

cookies = {
}

headers = {
    'Accept': 'application/json; application/vnd.esios-api-v1+json',
    'Content-Type': 'application/json',
    'Host': 'api.esios.ree.es',
    'Authorization': 'Token token="96b4d329e7efb4364fce1da618d7bc159b7f4463a23fc56ce19537d9"',
}

params = (
    ('start_date', '2021-11-02T00:00:00'),
    ('end_date', '2021-11-02T23:50:00'),
)

response = requests.get('https://api.esios.ree.es/indicators/1001', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.esios.ree.es/indicators/1001?start_date=2021-11-02T00:00:00&end_date=2021-11-02T23:50:00', headers=headers, cookies=cookies)

print (response.text)
a=response.text
print(type(a))

json_data = json.loads(response.text)


prueba1=json_data['indicator']
prueba2=prueba1['values']

df=pd.DataFrame(prueba2)

df2=df[df['geo_id']==8741]
