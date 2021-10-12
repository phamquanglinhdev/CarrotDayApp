import requests


class DataVideo:
    def __init__(self, category):
        self.videos = self.getCategories(category)

    def getCategories(self, category):
        header = {
            "name": category
        }
        response = requests.post("https://dl-devs.com/api/video/", data=header)
        print(response)
        return response.json()


class DataUserToken:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.result = self.signIn()

    def signIn(self):
        header = {
            "email": self.email,
            "password": self.password
        }
        url = "https://dl-devs.com/api/login"
        resource = requests.post(url, data=header)
        print(resource.json())
        return resource.json()


class User:
    def __init__(self, token):
        self.token = token
        self.result = self.getData(self.token)

    def getData(self, token):
        header = {
            "token": token
        }
        resource = requests.post("https://dl-devs.com/api/users", data=header)
        return resource.json()


# user = User("jzhzgxRG2zmCJAsMATSwd1Al6")
# print(user.result)
video = DataVideo("Python").videos
print(video)
