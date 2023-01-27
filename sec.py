import requests


# CIK number for Apple is 0001166559
cik_number = "0001166559"
url = f'https://data.sec.gov/submissions/CIK{cik_number}.json'
# add this
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1",
           "DNT": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
response = requests.get(url, headers=headers)
print(response.json()["cik"])
