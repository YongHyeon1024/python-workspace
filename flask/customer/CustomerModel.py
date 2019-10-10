import sqlite3

class Customer:
	name = ""
	gender = ''
	email = ""
	birthyear = 0
	
	def __init__(self, name, gender, email, birthyear):
		self.name = name
		self.gender = gender
		self.email = email
		self.birthyear = birthyear

class Model:
	customerList = []

	def insertCustsomer(self, data): # 입력
		self.customerList.append(Customer(data[0], data[1], data[2], data[3]))

	def deleteCustomer(self, email): # 삭제
		if len(self.customerList) != 0:
			for i, d in enumerate(self.customerList):
				if email == d.email:
					del self.customerList[i]
					break
	
	def updateCustsomer(self, data): # 수정
		if len(self.customerList) != 0:
			for i, d in enumerate(self.customerList):
				if data[2] == d.email:
					self.customerList[i].name = data[0]
					self.customerList[i].gender = data[1]
					self.customerList[i].birthyear = data[3]

	def loadSqlite3Data(self): # sqlite3 로드
		connect = sqlite3.connect("C:/Users/User/Documents/python-workspace/sqlite3Data.db")
		cursor = connect.cursor()
		sql = "SELECT * FROM CUSTOMER"
		cursor.execute(sql)
		dbData = cursor.fetchall()
		print(dbData)
		self.customerList.clear()
		for data in dbData:
			self.customerList.append(Customer(data[0], data[1], data[2], data[3]))
		connect.close()