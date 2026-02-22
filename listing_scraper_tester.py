import httpx
from lxml import html

url = "https://www.bezrealitky.cz/nemovitosti-byty-domy/856841-nabidka-pronajem-bytu-mikovcova-praha"
r = httpx.get(url)
tree = html.fromstring(r.text)

price = tree.xpath(
    '//div[contains(@class,"justify-content-between")]'
    '//strong[contains(@class,"h4 fw-bold")]//span/text()'
)

title_parts = tree.xpath('//h1//text()')
title = " ".join(t.strip() for t in title_parts if t.strip())

location = tree.xpath('//h1/span[contains(@class,"text-grey-dark")]/text()')
location = location[0].strip() if location else None

description_parts = tree.xpath(
    '//div[contains(@id,"english")]'
    '//p[contains(@class,"text-perex")]/text()'
)
description = "\n".join(d.strip() for d in description_parts if d.strip())

print(f"Title: {title}")
print(f"Price: {price[0]}")
print(f"Location: {location}")
print(f"Description: {description}")
