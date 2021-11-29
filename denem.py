html_doc = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>
    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="fred.jpg" alt="">
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>
</body>
</html>
"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
print(result)
result1 = soup.title
print(result1)
result2 = soup.head
print(result2)
result3 = soup.body
print(result3)
result4 = soup.title.name
print(result4)
result5 = soup.title.string
print(result5)

result6 = soup.h1
print(result6)
result7 = soup.h2
print(result7)
result8 = soup.h2.name
print(result8)
result9 = soup.h2.string
print(result9)
result10 = soup.h1.string
print(result10)

result11 = soup.find_all('h2')
print(result11)
result12 = soup.find_all('h2')[0]
print(result12)
result13 = soup.find_all('h2')[1]
print(result13)

result14 = soup.div
print(result14)
result15 = soup.find_all('div')[1]
print(result15)
result16 = soup.find_all('div')[1].ul.find_all('li')
print(result16)

result17 = soup.div.findChildren()
print(result17)

result18 = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
print(result18)

result19 = soup.find_all('a')
print(result19)

#for link in result:
#    print(link.get('href'))