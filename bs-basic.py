from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()


obj = BeautifulSoup(html_doc, "html.parser")


sonuc = obj
# prettify html dökümanını düzeltir.

sonuc = obj.prettify()
print(sonuc)


