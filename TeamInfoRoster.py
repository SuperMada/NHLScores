import requests

team = input("Please input team: ")

url = "https://statsapi.web.nhl.com/api/v1/teams/" + team + "/roster"

querystring = {"season":"20212022"}

response = requests.request("GET", url)

print(response.text)

data = response.text.split()

#Hi