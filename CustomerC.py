# 20190902a - 고객 정보 관리 시스템 RFP

import CustomerM
import CustomerV

class CustomerController:
	view = ""
	model = ""
	
	def __init__(self, view, model):
		self.view = view
		self.model = model

	def start(self):
		while True:
			selectMenu = self.view.menu()
			if selectMenu == 'I': # 고객 정보 입력
				customerData = self.view.insertCustsomer()
				self.model.insertCustsomer(customerData)

			elif selectMenu == 'C': # 현재 고객 정보 조회
				self.viewCustomer()

			elif selectMenu == 'P': # 이전 고객 정보 조회
				self.view.movePage(len(self.model.customerList), -1)
				self.viewCustomer()

			elif selectMenu == 'N': # 다음 고객 정보 조회
				self.view.movePage(len(self.model.customerList), 1)
				self.viewCustomer()

			elif selectMenu == 'F': # 전체 고객 정보 조회
				self.view.viewCustomer(self.model.customerList)

			elif selectMenu == 'U': # 고객 정보 수정
				select, setData = self.view.selectUpdateMenu()
				if select == "N":
					self.model.updateCustsomer(self.view.page, 0, setData)
				elif select == "G":
					self.model.updateCustsomer(self.view.page, 1, setData)
				elif select == "E":
					self.model.updateCustsomer(self.view.page, 2, setData)
				elif select == "B":
					self.model.updateCustsomer(self.view.page, 3, setData)

			elif selectMenu == 'D': # 고객 정보 삭제
				self.model.deleteCustomer(self.view.page)

			elif selectMenu == 'S': # 저장
				select = self.view.selectSaveLoadMenu()
				if select == 'P':
					self.model.savePickleData()
				elif select == 'S':
					self.model.saveSqlite3Data()

			elif selectMenu == 'L': # 불러오기
				select = self.view.selectSaveLoadMenu()
				if select == 'P':
					self.model.loadPickleData()
				elif select == 'S':
					self.model.loadSqlite3Data()

			elif selectMenu == 'Q': # 프로그램 종료
				break

	def viewCustomer(self):
		customerData = self.model.viewCustomer(self.view.page)
		if customerData:
			self.view.viewCustomer(customerData)
		

if __name__ == "__main__":
	View1 = CustomerV.CustomerView()
	Model1 = CustomerM.CustomerModel()
	Controller1 = CustomerController(View1, Model1)
	Controller1.start()
