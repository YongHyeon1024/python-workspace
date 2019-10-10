from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return "yonghyeon"

@app.route("/user/<username>")
def user(username):
	return "user %s" % username

@app.route("/user/<username>/<int:age>")
def user1(username, age):
	return render_template("index.html", username=username, age=age)

@app.route("/forminput/")
def forminput():
	return render_template("forminput.html")
	
@app.route("/method/", methods=["GET","POST"])
def method():
	if request.method == "POST":
		return "Post"
	else:
		return "Get"

@app.route("/form_input/")
def form_input():
	return render_template("form_input.html")

@app.route("/login/", methods=["POST"])
def login_post():
	username = request.form["username"]
	password = request.form["password"]
	return render_template("index1.html", username=username, password=password)


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000) # 기본 포트 5000
