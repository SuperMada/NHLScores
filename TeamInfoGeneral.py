import requests


def Clean(start, end):
    first = data.index(start)
    last = data.index(end)
    cut = (data[first:last])
    cut = str(cut)
    cut = cut.replace("[", "")
    cut = cut.replace("]", "")
    cut = cut.replace("\'", "")
    cut = cut.replace("\"", "")
    cut = cut.replace(",", "")
    return cut


def TeamName():
    name = Clean("\"name\"", "\"link\"")
    print("Team " + str(name.title()))


def ArenaName():
    name = [i for i, n in enumerate(data) if n == '\"name\"'][1]
    name_end = [i for i, n in enumerate(data) if n == '\"link\"'][1]
    arena = (data[name:name_end])
    arena = str(arena)
    arena = arena.replace("[", "")
    arena = arena.replace("]", "")
    arena = arena.replace("\'", "")
    arena = arena.replace("\"", "")
    arena = arena.replace(",", "")
    print("Arena " + str(arena.title()))


def CityName():
    origin = Clean("\"city\"", "\"timeZone\"")
    print(str(origin.title()))


team = input("Please input team: ")

url = "https://statsapi.web.nhl.com/api/v1/teams/" + team

querystring = {"season":"20212022"}

response = requests.request("GET", url)

#print(response.text)

data = response.text.split()

TeamName()
ArenaName()
CityName()


#print(str(data))


