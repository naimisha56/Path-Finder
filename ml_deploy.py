import requests



# Features order - "gender","ssc(percentage)","ssc(State or Others)","Inter(percentage)","Inter_board","Inter_Group","Branch","Internships","CGPA","skill"
# input format - [[feature values],[feature values]]
def predict_status_api(features):
    API_KEY = "VKOIS-OqmrTs9cSQBE_ru49tg0wFeNwSMQVOJwqbKXa4"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ["gender","ssc(percentage)","ssc(State or Others)","Inter(percentage)","Inter_board","Inter_Group","Branch","Internships","CGPA","skill"], "values": features}]}

    response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/03cbe867-0728-44c8-8997-7028e14e0826/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})

  

    data = response_scoring.json()['predictions'][0]['values']

    predictions = []

    for pred in data:
        
        predictions.append(pred[0])

    return predictions



def predict_salary_api(features):
    
    API_KEY = "VKOIS-OqmrTs9cSQBE_ru49tg0wFeNwSMQVOJwqbKXa4"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    
        
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    payload_scoring = {"input_data": [{"fields": ["gender","ssc(percentage)","ssc(State or Others)","Inter(percentage)","Inter_board","Inter_Group","Branch","Internships","CGPA","skill","status"], "values": features}]}

    response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/ac6e66ed-4f97-4016-b10c-09c4a14f1745/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    # print("Scoring response")
    # print(response_scoring.json())
    data = response_scoring.json()['predictions'][0]['values']

    predictions = []

    for pred in data:
        
        predictions.append(pred[0])

    return predictions