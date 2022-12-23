import requests

url = "https://instagram-scraper-2022.p.rapidapi.com/ig/followers/"

querystring = {"id_user": "528817151"}

headers = {
    "X-RapidAPI-Key": "17c1c2bc80msh0edbcbc5e8d8cbap178151jsnb0abea9d94a3",
    "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
