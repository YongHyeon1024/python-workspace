class CustomerView:
	page = 0

	# def __init__(self):
	# 	pass
	
	def menu(self): # 메뉴
		print('''
	I - 고객 정보 입력
	C - 현재 고객 정보 조회
	P - 이전 고객 정보 조회
	N - 다음 고객 정보 조회
	F - 전체 고객 정보 조회
	U - 고객 정보 수정
	D - 고객 정보 삭제
	S - 저장
	L - 불러오기
	Q - 프로그램 종료
	:''', end=' ')
		return input().upper()

	def setName(self):
		while True:
			name = input("이름: ")
			if len(name):
				return name

	def setGender(self):
		while True:
			gender = input("성별(F/M): ").upper()
			if gender == 'F' or gender == 'M':
				return gender

	def setEmail(self):
		while True:
			email = input("이메일: ")
			if len(email):
				return email

	def setBirthyear(self):
		while True:
			try:
				birthyear = int(input("생년(yyyy): "))
				if birthyear >= 0 and birthyear <= 9999:
					return  birthyear
			except Exception:
				pass
	
	def insertCustsomer(self): # 고객 정보 입력
		customerData = []
		customerData.append(self.setName())
		customerData.append(self.setGender())
		customerData.append(self.setEmail())
		customerData.append(self.setBirthyear())
		return customerData

	def movePage(self, dataLength, move): # 페이지 이동
		if (self.page + move) <= -1:
			print("처음 페이지")
			self.page = 0
		elif (self.page + move) >= dataLength:
			print("마지막 페이지")
			self.page = dataLength - 1
		else:
			self.page += move

	def viewCustomer(self, data): # 고객 정보 조회
		if isinstance(data, list):
			for data in data:
				print("이름: {0}, 성별: {1}, 이메일: {2}, 생년: {3}".format(data.name, data.gender, data.email, data.birthyear))
		else:
			print("이름: {0}, 성별: {1}, 이메일: {2}, 생년: {3}".format(data.name, data.gender, data.email, data.birthyear))

	def selectUpdateMenu(self):
		while True:
			select = input("선택: (N)이름, (G)성별, (E)이메일, (B)생년").upper()
			if select == "N":
				name = self.setName()
				return select, name
			if select == "G":
				gender = self.setGender()
				return select, gender
			if select == "E":
				email = self.setEmail()
				return select, email
			if select == "B":
				birthyear = self.setBirthyear()
				return select, birthyear

	def selectSaveLoadMenu(self):
		while True:
			select = input("선택: (P)pickle, (S)sqlite3\n").upper()
			if select == "P" or select == "S":
				return select