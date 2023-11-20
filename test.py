import requests

#Created a list of tuppels 
coordinates = []
coordinates.append((51.507359,-0.136439))

api_key = 'a6311858fb35df63b55216bae4aa952a'
mode = 'html'

endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0][0]}&lon={coordinates[0][1]}&appid={api_key}&mode={mode}"

print(endpoint)

#response = requests.get(endpoint)

#print(response.content)


