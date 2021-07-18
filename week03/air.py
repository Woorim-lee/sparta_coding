import requests
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#print(response_data)
#print(response_data.json())

city_air = response_data.json()
#print(city_air['RealtimeCityAir']['row'][0]['NO2'])

gu_infos = city_air['RealtimeCityAir']['row']

for gu_info in gu_infos:
    print(gu_info['MSRSTE_NM'], gu_info['PM10'])


#for gu_info in gu_infos:
#    if gu_info['PM10'] < 20:
#        print(gu_info['MSRSTE_NM'], gu_info['PM10'])