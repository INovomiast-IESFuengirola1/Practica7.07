import os
import platform

#Test username extraction from Device for paths:
username = os.getlogin()

print(username)

#Test get current dir:

cwd = os.getcwd()
print(cwd)

#Check OS type:
print(platform.system())

