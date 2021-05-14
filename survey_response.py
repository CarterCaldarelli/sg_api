import requests
import json
import pandas as pd  
from pandas import json_normalize

#Declare url and set headers and parameters
url = 'https://restapi.surveygizmo.com/v4/survey/5888411/surveyresponse?api_token=[my_token]&api_token_secret=[my_secret_token]'
headers = {
			'Content-Type': 'application/json',
			'Cache-Control': 'no-cache'
			}
params = { 
			'resultsperpage' : '500'
			}
#GET request to retrieve number of API pages
response = requests.get(url, headers = headers, params = params)
response = response.json()
page_count = response['total_pages']
print(page_count)

#Create list length of page count
l = []
x = 0
while x < page_count:
	x = x + 1
	l.append(x)

#Iterate through API pages and create csv files of each page.  
y = 1
while y <= page_count:
	for i in l:
		url = 'https://restapi.surveygizmo.com/v4/survey/5888411/surveyresponse?api_token=[my_token]&api_token_secret=[my_secret_token]'
		headers = {
			'Content-Type': 'application/json',
			'Cache-Control': 'no-cache'
			}
		params = { 
			'resultsperpage' : '500',
			'page': str(y)
			}
		response = requests.get(url, headers = headers, params = params)
		response = response.json()
		response = response['data']
		response = json_normalize(response)
		df = pd.DataFrame(response)
		df.to_csv('cp'+str(i)+'.csv')
		print('Page '+ str(y) +' complete')
		y = y + 1

#if first file, read file in as dataframe, else append to previous file.
	for i in l:
		if i == 1:
			df = pd.read_csv('C:\\Users\\ccaldarelli\\pyscripts\\cp'+str(i)+'.csv')
			print('First file read')
		else:
			df_a = pd.read_csv('cp'+str(i)+'.csv')
			appended = df_a.append(df)
			df = appended
			print('File appended')
pbi_table = df
