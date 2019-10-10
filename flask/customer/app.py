from flask import Flask, render_template, request, redirect
import CustomerModel

app = Flask(__name__)

@app.route('/') # index
def index():
	return render_template("index.html")

@app.route("/customertable") # 전체 조회
def customerView():
	dataTable = model.customerList
	return render_template("customertable.html", result=dataTable)

@app.route("/customertable", methods=["POST"])
def customerTable():
	if request.method == "POST":
		print(request.form)
		if request.form["button"] == "I": # 입력
			name = request.form["name"]
			gender = request.form["gender"]
			email = request.form["email"]
			birthyear = request.form["birthyear"]
			model.insertCustsomer([name, gender, email, birthyear])
		if request.form["button"] == "U": # 업데이트
			name = request.form["name"]
			gender = request.form["gender"]
			email = request.form["email"]
			birthyear = request.form["birthyear"]
			model.updateCustsomer([name, gender, email, birthyear])
		if request.form["button"] == "D": # 삭제
			model.deleteCustomer(request.form["email"])
			
	return redirect("/customertable")

@app.route("/customerupdate") # 업데이트
def customerupdate():
	return render_template("customertable.html")

@app.route("/customerdelete") # 삭제
def customerdelete():
	return redirect("/customertable")

@app.route("/datasave")
def datasave():
	return render_template("index.html")
	
@app.route("/dataload")
def dataload():
	model.loadSqlite3Data()
	return redirect("/customertable")

if __name__ == "__main__":
	model = CustomerModel.Model()
	app.run(debug=True, host="0.0.0.0", port=5000) # 기본 포트 5000