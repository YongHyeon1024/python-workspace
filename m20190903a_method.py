import random

def setName(dataList): # 제목, 이름 입력
	while True:
		dataList["title"] = input("게임의 제목 입력\n: ")
		if len(dataList["title"]) and len(dataList["title"]) <= 25:
			break
		print("오류")
	while True:
		dataList["name"] = input("게이머의 이름을 입력하세요\n: ")
		if len(dataList["name"]):
			break
		print("오류")

def inputNumber(): # 숫자 입력
	while True:
		try:
			gamerNumber = int(input("0~99사이의 값으만 AI의 값을 예측하여 입력하세요\n: "))
		except:
			print("오류")
			continue
		if gamerNumber >= 0 and gamerNumber <= 99:
			break
		print("오류")
	return gamerNumber

def game1(gamerNumber, randomNumber):
	if gamerNumber == randomNumber:
		print("정답")
		return False
	elif gamerNumber < randomNumber:
		print("    보다 큼")
		return True
	elif gamerNumber > randomNumber:
		print("    보다 작음")
		return True

def gamePlay(dataList): # 게임 진행
	gameReplay = True
	while gameReplay:
		randomNumber = random.randrange(0, 99)
		gameAttempt = 0
		gameStatus = True
		while gameStatus:
			gameAttempt += 1
			gamerNumber = inputNumber()
			gameStatus = game1(gamerNumber, randomNumber)
		print("시도 횟수: {0}".format(gameAttempt))
		dataList["score"] = 100 / gameAttempt
		print("점수: {0:0.1f}".format(dataList["score"]))
		dataList["total"] += dataList["score"]
		gameReplay = gameReplayCheck()

def gameReplayCheck(): # 게임 재시작 체크
	while True:
		inputCheck = input("게임 재시작(R) 게임 끝내기(Q)\n: ").upper()
		if inputCheck == "R":
			return True
		elif inputCheck == "Q":
			return False
		print("오류")