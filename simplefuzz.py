 import requests

url = "https://google.com"

with open(r'wordlist.txt','r') as wlist:  
  for i in wlist:
    wl = i.strip()
    try:
      req = requests.get(url+wl)
      print(f"status code {req.status_code}", url + wl)
    except:
      print("something went wrong")
