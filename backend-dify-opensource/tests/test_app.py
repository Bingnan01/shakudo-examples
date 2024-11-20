# # curl "http://0.0.0.0:8000/recommendTables?prompt=get+me+all+tables&schema=public"

# avenue_llama3_pov

# import requests
# url = "http://0.0.0.0:8000/recommendTables"

# data = {
#   "prompt": "what are top 5 country in climate change metadata table?",
#   "schema": "climate",
# }

# response = requests.get(url, params=data)
# print(response.json())


# import requests

# url = "http://hyperplane-service-016559.hyperplane-pipelines.svc.cluster.local:8787/generateSQL"

# # # Pass data as JSON body
# data = {
#     "prompt": "what are top 5 country in climate change metadata table?",
#     "schema": "climate",
#     "tables": ["climate_change_data_metadata"]
# }

# response = requests.post(url, json=data)  # Use POST and send JSON body
# print(response.json())


import requests

# Define the URL of your endpoint
url = "http://0.0.0.0:8000/validateAndExecuteSQL"

# Define the SQL code to validate and execute
data = {
    "data": "SELECT COUNT(*) FROM climate.climate_change_data_metadata;"
}

# Send a GET request with the SQL code as a query parameter
response = requests.post(url, json=data) 

# Print the response from the server
print(response.json())


