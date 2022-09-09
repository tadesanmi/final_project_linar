# A program that verifies password
import getpass
database = {"tadesanmi": "123456", "t.adesanmi": "654321"}
username = input("enter your username: ")
password = getpass.getpass("enter your password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("enter your password again :")
        break
print("verified")