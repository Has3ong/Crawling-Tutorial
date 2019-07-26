from urllib import request
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_url = 'data:image/png;base64,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'
html_url = 'http://google.com'

savePath_1 = BASE_DIR + '/2-1/test.jpg'
savePath_2 = BASE_DIR + '/2-1/index.html'

try:
    filename1, headers1 = request.urlretrieve(img_url, savePath_1)
    filename2, headers2 = request.urlretrieve(html_url, savePath_2)

except Exception as e:
    print('Failed : ', e)

else:
    print(headers1)
    print(headers2)
