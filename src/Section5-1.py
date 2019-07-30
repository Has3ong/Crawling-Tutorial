from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>BeautifulSoup Example</title>
    </head>
    <body>
        <h1>H1 Tag</h1>
        <h2>H2 Tag</h2>
        <p class="A">First P Tag</p>
        <p class="B">Second P Tag</p>
        <p id="C"> Third P Tag
            <p class = "D">Multiple P Tag</p>
        </p>
        <p class="A">Fourth P Tag</p>
    </body>
</html>
"""

print('\n# soup')
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
print(soup.prettify())

print('\n# h1\n')
h1 = soup.html.body.h1
print(h1)

print('\n# p1')
p1 = soup.html.body.p
print(p1)
print(p1.string)

print('\n# p2')
p2 = p1.next_sibling.next_sibling
print(p2)
print(list(p2.next_elements))

soup = BeautifulSoup(html, 'html.parser')
p3 = soup.find_all("p")  # limit=2
print('\n# p3')
type((p3))
print(p3)

print('\n# link')
# class Selector
link1 = soup.select_one("p.A")
# id Selector
link2 = soup.select_one("p#C")

print(link1)
print(link1.string)
print(link2)
print(link2.string)


print('\n# link2')
link1 = soup.select("p.A")
print(link1)
print(link1[0], link1[1])
print(link1[0].contents)