# pip install beautifulsoup4
# html parser

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())
print(soup.title)
print(soup.p)
print(soup.find("p", "story").text)  # 첫번째 인자는 태그, 두번째 인자는 class

# 크롤링/스크랩핑 하려는 도메인에서 robots.txt를 반드시 확인할 것.
# 크롤링/스크래핑 하면 안 되는 디렉토리 목록을 작성해놓음. ex) inflearn.com/robots.txt
