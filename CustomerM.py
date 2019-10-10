import pickle, sqlite3

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

class CustomerModel:
	customerList = []

	# def __init__(self):
	# 	pass

	def insertCustsomer(self, data): # 고객 정보 입력
		self.customerList.append(Customer(data[0], data[1], data[2], data[3]))

	def viewCustomer(self, page): # 고객 정보 조회
		if len(self.customerList) != 0:
			return self.customerList[page]
		return False

	def updateCustsomer(self, page, switch, data):
		if switch == 0:
			self.customerList[page].name = data
		if switch == 1:
			self.customerList[page].gender = data
		if switch == 2:
			self.customerList[page].email = data
		if switch == 3:
			self.customerList[page].birthyear = data

	
	def deleteCustomer(self, page): # 고객 정보 삭제
		if len(self.customerList) != 0:
			del self.customerList[page]
	
	def savePickleData(self): # pickle 세이브
		if len(self.customerList) != 0:
			with open("pickleData.bin", "wb") as f:
				pickle.dump(self.customerList, f)

	def loadPickleData(self): # pickle 로드
		with open("pickleData.bin", "rb") as f:
			self.customerList = pickle.load(f)
	
	def saveSqlite3Data(self): # sqlite3 세이브
		if len(self.customerList) != 0:
			connect = sqlite3.connect("./sqlite3Data.db")
			cursor = connect.cursor()
			sql = """
				CREATE TABLE IF NOT EXISTS "CUSTOMER" (
				name TEXT, 
				gender TEXT,
				email TEXT,
				birthyear INTEGER
				)
				"""
			cursor.execute(sql)
			connect.commit() # 커밋
			sql = "INSERT INTO CUSTOMER (name, gender, email, birthyear) VALUES "
			for data in self.customerList:
				sql += """
				("{0}", '{1}', "{2}", {3}), 
				""".format(data.name, data.gender, data.email, data.birthyear)
			sql = sql[:sql.rfind(',')] + sql[(sql.rfind(',') + 1)]
			cursor.execute(sql)
			connect.commit() # 커밋
			connect.close()

	def loadSqlite3Data(self): # sqlite3 로드
		connect = sqlite3.connect("./sqlite3Data.db")
		cursor = connect.cursor()
		sql = "SELECT * FROM CUSTOMER"
		cursor.execute(sql)
		dbData = cursor.fetchall()
		self.customerList.clear()
		for data in dbData:
			self.customerList.append(Customer(data[0], data[1], data[2], data[3]))
		connect.close()
