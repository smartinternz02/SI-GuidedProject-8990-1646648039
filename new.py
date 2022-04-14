import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "yRrxWYCduJe9oe664g4jPMnAK7oEXdcycNCMXbaFuYov"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['_id','cycles_per_minute','set1','set2','set3','sen1','sen2','sen3','sen4','sen5','sen6','sen7','sen8','sen9','sen10','set11','set12','set13','set14','set15','set16','set17','set18','set19','set20','trajectory']], "values": [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f68f290f-c805-428c-b12a-cc0bedd30fce/predictions?version=2021-10-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions = response_scoring.json()

print("Scoring response")
predictions=response_scoring.json()
#print(predictions)
pred=predictions['predictions'][0]['values'][0][0]
if(pred == 0):
    #pred = "No failure expected within 30 days."
    print("No failure expected within 30 days.") 
else:
     #pred = "Maintenance Required!! Expected a failure within 30 days.
     print("Maintenance Required!! Expected a failure within 30 days.")