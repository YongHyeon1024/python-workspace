import requests, csv, sqlite3
from bs4 import BeautifulSoup

url = "https://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1171010400"
requestData = requests.get(url)
html = requestData.text
soup = BeautifulSoup(html, "html.parser")

data1 = []
data2 = [[0 for x in range(2)] for y in range(30)]

data1 += [soup.find_all("a", {"class" : "sale_title"})]
data1 += [soup.find_all("td", {"class" : "num align_r"})]

t1 = []
for d in data1[0]:
	t1 += [d.text]
data1[0] = t1
t1 = []
for d in data1[1]:
	t1 += [d.text.split('\n')[2]]
	
data1[1] = t1

for i1, d1 in enumerate(data1):
	for i2, d2 in enumerate(d1):
		data2[i2][i1] = d2

for d in data2:
	print(d)

# with open("./csvfile.csv", "w", newline='') as f: # csv 파일 저장
# 	w = csv.writer(f)
# 	for d in data2:
# 		w.writerow(d)
	
# connect = sqlite3.connect("./sqlite3file.db") # db 저장
# cursor = connect.cursor()
# sql = """
# 	CREATE TABLE IF NOT EXISTS "t1" (
# 	d1 TEXT, 
# 	d2 TEXT, 
# 	d3 TEXT, 
# 	d4 TEXT, 
# 	d5 TEXT, 
# 	d6 TEXT
# 	)
# 	"""
# print(sql)
# cursor.execute(sql)
# connect.commit() # 커밋
# sql = "INSERT INTO t1 (d1, d2, d3, d4, d5, d6) VALUES "
# for d in data2:
# 	sql += """
# 	("{}", "{}", "{}", "{}", "{}", "{}"), 
# 	""".format(d[0], d[1], d[2], d[3], d[4], d[5])
# sql = sql[:sql.rfind(',')]
# print(sql)
# cursor.execute(sql)
# connect.commit() # 커밋
# connect.close()