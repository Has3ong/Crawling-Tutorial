from urllib import request
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

path = ['/2-2/test.jpg', '/2-2/test.html']
target_url = ["https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbvkhQ9%2FbtqvXwaw3vP%2FJtvtY3jQLS3w0XYaQe8fE1%2Fimg.jpg",
              "http://google.com"]

cnt = 0
for i in target_url:
    try:
        response = request.urlopen(i)
        contents = response.read()

        with open(os.path.join(BASE_DIR + path[cnt]), "wb") as f:
            f.write(contents)

    except Exception as e:
        print('Error Code : ', e)

    else:
        print()
        print("Download Succeed.")
        cnt += 1
