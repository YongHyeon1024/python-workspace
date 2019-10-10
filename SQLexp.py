import sqlite3

conn = sqlite3.connect('sqlite3Data.db') # db 파일 생성
c = conn.cursor()
c.execute() # sql 실행
c.fetchall # 커서의 모든 데이터 가져오기
conn.commit() # 커밋
conn.close()