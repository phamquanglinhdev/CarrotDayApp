import os

from Database import User


class LocaL:
    def __init__(self):
        self.dir = "C://ProgramData/PQLdev/CarrotDay"
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def setToken(self, token):
        path = self.dir + "token.txt"
        file = open(path, "w+")
        file.write(token)
        print("saving token:" + token)
        file.close()

    def checkToken(self):
        path = self.dir + "token.txt"
        create = open(path, "a")
        file = open(path, "r+")
        token = file.read()
        result = User(token).result
        results = {"code": result["code"], "token": token}
        print(results["code"])
        file.close()
        return results

    def destroyToken(self):
        path = self.dir + "token.txt"
        destroy = open(path, "w+")
        destroy.close()

    # print(col)
    # file.close()


test = LocaL()
test.checkToken()
