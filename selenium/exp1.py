# from bs4 import BeautifulSoup
# import requests

# starbugs = requests.get('https://www.istarbucks.co.kr/store/store_map.do')
# st_bs=BeautifulSoup(starbugs.text,'lxml')
# print(st_bs.select('li.quickResultLstCon'))

import urllib.request
import os

#이미지의 주소
url='https://i-h2.pinimg.com/474x/ac/b9/eb/acb9eb2a70dd9c342c90598a5f20bf72.jpg?b=t'

#실행하는 파일의 경로를 찾아서 같은 경로에 이미지 저장
dirname=os.path.dirname(__file__)
savename=dirname +'/test.png'
'''
# 파일로 저장
urllib.request.urlretrieve(url,savename)
'''
# 파일을 열고.. 활용 할수 있다.
mem = urllib.request.urlopen(url).read()

# 위에서 불러온 파일을 저장함.

print(savename)
with open(savename,mode='wb') as f:
    f.write(mem)
    print('저장되었습니다.')
