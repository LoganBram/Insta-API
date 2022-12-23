import requests


class User:
    def __init__(self, username):
        self.username = username

    def GetID(self):
        # obtain user ID using instagram API
        url = "https://instagram-scraper-2022.p.rapidapi.com/ig/user_id/"

        querystring = {"user": self.username}

        headers = {
            "X-RapidAPI-Key": "17c1c2bc80msh0edbcbc5e8d8cbap178151jsnb0abea9d94a3",
            "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        self.id = response.json()["id"]
        print(self.id)

    def GetFollowers(self):
        url = "https://instagram-scraper-2022.p.rapidapi.com/ig/followers/"

        querystring = {"id_user": self.id}

        headers = {
            "X-RapidAPI-Key": "17c1c2bc80msh0edbcbc5e8d8cbap178151jsnb0abea9d94a3",
            "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        print(response.json()["users"][1])


def main():

    # username = input("whats your username?")
    username = "maligoshik"
    user = User(username)
    user.GetID()
    user.GetFollowers()


main()
