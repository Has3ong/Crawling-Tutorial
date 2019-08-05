# Crawling_Basic_1

#### Runtime Enviroment
```
macOS Mojave 10.14.5
```

#### Crawling vs Scraping
##### Scraping
* A technology that automatically extracts and collects information located on a desired part of a website on a computer
##### Crawling
* Browsing multiple webpages in accordance with established rules by the web crawler, an automated bot
* ex 구글봇(Googlebot)

#### HTML TAG

```
<!DOCTYPE html>
    <html>
        <head>
            <title>My First Title</title>
        </head>
        <body>
            <h1>My First Heading</h1>
            <p>My first paragraph.</p>
        </body>
</html>
```

#### Chrome Development Tools

<img width="600" src="https://user-images.githubusercontent.com/44635266/61855741-9c129a80-aefb-11e9-9cdf-c8e9174b392d.png">

```
> fn + F12
> Command + Shift + C

# CSS Selector
#news_cast > div.area_newstop > div > div > ol

# JS Path
document.querySelector("#news_cast > div.area_newstop > div > div > ol")

# XPath
//*[@id="news_cast"]/div[1]/div/div/ol
```