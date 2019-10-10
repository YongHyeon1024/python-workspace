import requests, csv, sqlite3
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/point/af/list.nhn" # ["번호", "평점", "영화", "140자평", "글쓴이", "날짜"]
requestData = requests.get(url)
html = requestData.text
soup = BeautifulSoup(html, "html.parser")

data1 = []
data2 = [[0 for x in range(6)] for y in range(10)]

data1 += [soup.find_all("td", {"class" : "ac num"})]
data1 += [soup.find_all("td", {"class" : "point"})]
data1 += [soup.find_all("a", {"class" : "movie"})]
data1 += [soup.find_all("td", {"class" : "title"})]
data1 += [soup.find_all("a", {"class" : "author"})]
data1 += [soup.find_all("td", {"class" : "num"})]

t1 = []
for d in data1[0]:
	t1 += [d.text]
data1[0] = t1
t1 = []
for d in data1[1]:
	t1 += [d.text]
data1[1] = t1
t1 = []
for d in data1[2]:
	t1 += [d.text]
data1[2] = t1
t1 = []
for d in data1[3]:
	t1 += [d.text.split('\n')[2]]
data1[3] = t1
t1 = []
for d in data1[4]:
	t1 += [d.text]
data1[4] = t1
t1 = []
for i, d in enumerate(data1[5]):
	if i % 2 == 0:
		continue
	t1 += [d.text.split("****")[1]]
data1[5] = t1

for i1, d1 in enumerate(data1):
	for i2, d2 in enumerate(d1):
		data2[i2][i1] = d2

for d1 in data2:
	print(d1)

# with open("./csvfile.csv", "w", newline='') as f: # csv 파일 저장
# 	w = csv.writer(f)
# 	for d in data2:
# 		w.writerow(d)
	
connect = sqlite3.connect("./sqlite3file.db") # db 저장
cursor = connect.cursor()
sql = """
	CREATE TABLE IF NOT EXISTS "t1" (
	d1 TEXT, 
	d2 TEXT, 
	d3 TEXT, 
	d4 TEXT, 
	d5 TEXT, 
	d6 TEXT
	)
	"""
print(sql)
cursor.execute(sql)
connect.commit() # 커밋
sql = "INSERT INTO t1 (d1, d2, d3, d4, d5, d6) VALUES "
for d in data2:
	sql += """
	("{}", "{}", "{}", "{}", "{}", "{}"), 
	""".format(d[0], d[1], d[2], d[3], d[4], d[5])
sql = sql[:sql.rfind(',')]
print(sql)
cursor.execute(sql)
connect.commit() # 커밋
connect.close()