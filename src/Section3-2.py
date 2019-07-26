
import urllib.request
import urllib.parse

# 행정 안전부 : https://www.mois.go.kr
URL = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012"

params = []
res_data = urllib.request.urlopen(URL).read()
contents = res_data.decode("utf-8")
print(contents)