# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sriya" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/mypage")
def mypage():
    return render_template("index.html",variable = "father")

# define the route to mother webpage
@app.route("/motherwebpage")
def motherwebpage():
    return render_template("index.html",variable = "mother")

# define the route to friends webpage
@app.route("/friendspage")
def friendpage():
    return render_template("index.html",variable = "friend")

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
