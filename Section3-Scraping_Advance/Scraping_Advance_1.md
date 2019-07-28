# Scraping_Advance_1

#### GET Response

```
> Section3-1.py

import urllib.request
from urllib.parse import urlparse

url = "https://github.com/Has3ong/"

git = urllib.request.urlopen(url)

print('type : {}'.format(type(git)))
print("URL : {}".format(git.geturl()))
print("HTTP Status code : {}".format(git.status))
print("Headers : {}".format(git.getheaders()))
print("HTTP Get code : {}".format(git.getcode()))
print('parse : {}'.format(urlparse('https://github.com/Has3ong/?test=test').query))

API = "https://api.ipify.org"
values = {
    'format': 'json'
}

params = urllib.parse.urlencode(values)
url = API + "?" + params
print("Response URL= {}".format(url))

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print('response : {}'.format(text))

```

* urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
```
Parse a URL into six components, returning a 6-item named tuple.
This corresponds to the general structure of
a URL: scheme://netloc/path;parameters?query#fragment.
Each tuple item is a string, possibly empty.
```

#### RSS File Check

* RSS (Rich Site Summary) is a content expression method that is mainly used in news and blog sites. 
* The website administrator shows the content of the website in RSS format.
* Since automatic collection using RSS-related programs (or services) is possible,
the user can view the latest information without having to visit each site in one place.

<img width="600" src="https://user-images.githubusercontent.com/44635266/61959783-1e37b780-afff-11e9-9c05-da4ebb6dd5e5.png">

```
Section3-2.py

import urllib.request
import urllib.parse

# 행정 안전부 : https://www.mois.go.kr
URL = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012"

params = []
res_data = urllib.request.urlopen(URL).read()
contents = res_data.decode("utf-8")
print(contents)
```

* Output
```
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:taxo="http://purl.org/rss/1.0/modules/taxonomy/"
    xmlns:activity="http://activitystrea.ms/spec/1.0/" >
<channel>
<title>보도자료</title>
<link>https://www.mois.go.kr</link>
<description></description>
<language>ko</language>
<pubDate>FRI, 26 JUL 2019 10:00:00 KST</pubDate>

...

<item>
            <title><![CDATA[어린이보호구역 교통사고 87%가 보행 중 발생]]></title>
            <link><![CDATA[https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=71980]]></link>
            <description><![CDATA[
                어린이보호구역 교통사고 87%가 보행 중 발생<br />- 행안부, 관계기관과 함께 교통사고 다발 어린이보호구역 점검 실시 -<br /><br />□ 행정안전부(장관 진영)는 7월 22일부터 26일까지 교통사고가 잦은 어린이보호구역에 대해 관계기관* 합동으로 점검을 실시하여 근본적인 개선대책을 마련한다.<br />    * 행정안전부, 교육부, 경찰청, 지자체, 도로교통공단<br /> ○ 이번 점검은 어린이보호구역으로 지정된 16,765개소 중 지난해 교통사고가 2건 이상 발생하였거나 사망사고가 발생한 교통사고 다발 구역 42개소를 대상으로 한다.<br /><br />□ 2018년 어린이보호구역에서 발생한 교통사고는 총 435건이며,   사고특성을 살펴보면 다음과 같다. <br /> ○ 보행 중 사고가 377건(87%)으로 대부분을 차지했고 주로 방과 후 집으로 귀가하거나 학원으로 이동하는 시간대인 오후 2시에서 6시 사이에 239건(55%)으로 가장 많이 발생했다.<br /> ○ 월별로는 4월에 54건(12%), 5월에 48건(11%), 7월에 46건(11%), 순으로 어린이들의 야외 활동이 많은 시기에 사고도 많은 것으로 나타났다.<br /> ○ 요일별로는 화요일과 금요일이 각 87건(20%)으로 가장 많았고 학교에 가지 않는 토요일(31건)과 일요일(22건)이 상대적으로 적었다.<br /> ○ 사망사고는 총 3건이 발생했는데 4～5월 중 화요일 오후 2~6시 사이에 발생하였으며 모두 초등학교 1학년생이었다.<br /><br />□ 행정안전부는 이번 점검을 통해 교통사고 다발 어린이보호구역의교통안전시설 진단, 주변 환경요인 점검 등 사고 원인을 종합적으로 분석하고 실효성 있는 개선방안을 마련하고 빠른 시일 내에 시설 개선을 완료한다는 방침이다.<br /><br />□ 조상명 행정안전부 생활안전정책관은 “정부와 지자체의 꾸준한 노력으로 어린이 교통사고가 지속적으로 줄어들고는 있으나 개선해야 할 부분들이 아직 많다.”라며, “교통사고가 빈번한 곳에 대해서는 철저한 원인분석을 통해 조속히 개선할 계획이다.”라고 말했다.<br /><br />* 담당 : 안전개선과 권순관(044-205-4219)
                    ]]></description>
            <pubDate>SUN, 21 JUL 2019 12:00:00 KST</pubDate>
            <author>안전개선과</author>
        </item>
    
</channel>
</rss>

```