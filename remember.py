import os

dir = "C:/ProgramData/PQLdev/CarrotDay"
if not os.path.exists(dir):
    os.makedirs(dir)
else:
    path = dir + "token.txt"
    file = open(path, "w")
    file.close()
