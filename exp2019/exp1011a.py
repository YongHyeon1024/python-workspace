'''
tips 데이터
ex1) 요일별 팁의 액수를 합산하여 막대그래프 시각화(1인, 6인 파티는 제외)
ex2) 요일별 파티 사이즈별 타피 횟수 카운트하여 막대그래프 시각화(size2,3,4인만 카운트)

영화 평점 데이터(movielens)
영화 평점 데이터를 활용하여 다움을 실시해보세요

1. 데이터 탐색 : NA처리
2. 영화별 성별 평점 평균을 산출하여 성별로 상위/하위 10개 영화의 목록 추출 및 도식화
3. 영화 평점 정보가 300건 이상 있는 영화에 대하여 여성에게 인기가 높은 상위 10개 영화
4. 남녀간 호불호가 큰 영화는?
5. 성별에 관계없이 호불호가 큰 영화는?
'''

import pandas as pd

dataList1 = []
dataList2 = []
dl1 = dataList1
dl2 = dataList2
readcsv = pd.read_csv('c:/data/tips.csv')
df = pd.DataFrame(readcsv)
dl1.append(df)
dl2.append(df)

# ex1
dl1.append(dl1[0][['day', 'size']])  # 제외
dl1[1] = dl1[1][dl1[1]['size'] != 1]
dl1[1] = dl1[1][dl1[1]['size'] != 6]
# dl.append()

print(pd.concat(dl1[1], axis=0))
