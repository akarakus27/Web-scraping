import requests
from bs4 import BeautifulSoup

headers_param = {"User-Agent":" Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
glassdor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm", headers=headers_param)

print(glassdor.status_code)
