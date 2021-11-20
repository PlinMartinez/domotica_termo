# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:02:21 2021

Se conecta a ESIOS para sacar los costes por hora de la electricidad

@author: Plin Martinez
"""

from datetime import datetime, date, timedelta
import pandas as pd
import requests
import json
#from clavero import token
token='"c125d37896b4d329e7efb4364fce1da618d7bc159b7f4463a23fc56ce19537d9"'

cookies = {
}

#prepara los headers para la consulta con el token que piden a las electricas

headers = {
    'Accept': 'application/json; application/vnd.esios-api-v1+json',
    'Content-Type': 'application/json',
    'Host': 'api.esios.ree.es',
    'Authorization': 'Token token='+token,
}

# SACA LA FECHA DE HOY Y MAÑANA, SI ES PRONTO TRABAJA COSTES DEL DIA, SI ES TARDE MIRA MAÑANA
fecha=datetime.now()
hoy=date.today()
hora=fecha.hour
one_day=timedelta(days=1)
mañana=hoy+one_day

if hora > 22 :
    fecha_consulta=mañana
    
else:
    fecha_consulta=hoy

print("lanzamos la consulta a fecha de ",fecha_consulta)

inicio='T00:00:00'
fin='T23:50:00'


tupla1=('start_date',str(fecha_consulta)+inicio)
tupla2=('end_date',str(fecha_consulta)+fin)
params=(tupla1,tupla2)

#recibe la respuesta y la empieza a ordenar para sacar los valores utiles

response = requests.get('https://api.esios.ree.es/indicators/1001', headers=headers, params=params, cookies=cookies)

json_data = json.loads(response.text)

prueba1=json_data['indicator']
prueba2=prueba1['values']

df=pd.DataFrame(prueba2)

df2=df[df['geo_id']==8741]

df2['date']=pd.to_datetime(df['tz_time'])
df2['hora']=df2['date'].dt.hour


print(df2.dtypes)


df2.drop(columns=['datetime','datetime_utc'])


df2.drop(['datetime','datetime_utc','tz_time','geo_id','geo_name'],axis=1,inplace=True)

df3=df2[['date','hora','value']]



print (df3)
