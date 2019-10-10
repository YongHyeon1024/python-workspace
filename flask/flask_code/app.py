from flask import Flask, render_template,request

app=Flask("ㅅㅊㅎ")

@app.route('/')
def index():
    return "hello world 손정현"

@app.route('/cakes/')
def cakes():
    return "yummy cakes!!"

@app.route('/user/<username>')
def user(username):
    return 'user %s' % username

@app.route('/user/<username>/<int:age>')
def user1(username,age):
    # return 'username %s , age %d' %(username,age)
    return render_template('index.html',username=username,age=age)

@app.route('/forminput/')
def forminput():
    return render_template('forminput.html')    

@app.route('/method/', methods=['GET','POST'])
def method():
    if request.method=='POST':

        return "Post"
    else:
        return "Get"

@app.route('/login/')
def login():
    # http://127.0.0.1:5000/login?name=hong
    username = request.args.get('name')
    print("login ->", username)
    return render_template('index.html',username=username)

@app.route('/forminput1/')
def forminput1():
    return render_template('forminput1.html') 

@app.route('/form_input/')
def form_input():
    return render_template('form_input.html')

@app.route('/login/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    return render_template('index.html',username=username,password=password)

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port = 8089)
