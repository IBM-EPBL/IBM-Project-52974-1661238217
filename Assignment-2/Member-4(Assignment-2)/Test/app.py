from flask import Flask,render_template,request


app=Flask(__name__)



@app.route("/")
def home():
    return render_template("home.htm")



   

@app.route("/signup")

def signup():
    return render_template("signup.htm")

@app.route('/register',methods=['POST','GET'])

def register():


    if request.method == 'POST':
        n=request.form.get('name')
        e=request.form.get('email')
        h=request.form.get('phone')
        p=request.form.get('password')
    return render_template('register.htm',name=n,email=e,phone=h,password=p)
  
@app.route("/signin")
def signin():
    return render_template("signin.htm")


@app.route("/about")
def about():
    return "<h1>About Page </h1>"


if __name__=='__main__':
    app.run(debug=True)