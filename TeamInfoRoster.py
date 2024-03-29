import requests


def PrintRoster():
    name_end = [i for i, n in enumerate(data) if n == '\"link\"'][-2]
    counter = 0
    name = 0

    while (name + 4 != name_end):
        name = [i for i, n in enumerate(data) if n == '\"fullName\"'][counter]
        full_end = [i for i, n in enumerate(data) if n == '\"link\"'][counter]
        full_name = (data[name:full_end])
        full_name = str(full_name)
        full_name = full_name.replace("[", "")
        full_name = full_name.replace("]", "")
        full_name = full_name.replace("\'", "")
        full_name = full_name.replace("\"", "")
        full_name = full_name.replace(",", "")
        print(str(full_name.title()))
        counter += 1

def PosNumbers():
    defence = data.count("\"D\"")
    left = data.count("\"LW\"")
    right = data.count("\"RW\"")
    center = data.count("\"C\"")
    goalie = data.count("\"G\"")
    print("Defencemen: " + str(defence) + "\n" + "Left Wingers: " + str(left) + "\n" + "Right Wingers: " + str(right) + "\n" + "Centers: " + str(center) + "\n" + "Goalies: " + str(goalie))




team = input("Please input team: ")

url = "https://statsapi.web.nhl.com/api/v1/teams/" + team + "/roster"

querystring = {"season":"20212022"}

response = requests.request("GET", url)

#print(response.text)

data = response.text.split()

PrintRoster()
PosNumbers()
