from m20190903a_method import *

if __name__ == "__main__":
	dataList = {"title":"", "name":"", "score":0, "total":0}
	setName(dataList)
	print("================== = " + dataList["title"] + " == = v1.0.0 == ==================")
	gamePlay(dataList)
	print("총점: {0:0.1f}".format(dataList["total"]))