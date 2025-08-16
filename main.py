#print("Hello World")
#whenever we create a project we create virtual enviornment bcoz every time we create a project python version changes 
#to ensure the failuer to run the project
#python -m venv myenv   -> to create a virtual environment  #env
#to activate the env created: .\myenv\Scripts\activate
#to deactivate: just write deactivate
#pip is python package manager -> any package install, any library uninstall or upgrade we use pip

#to create flask application

#import flask first
from flask import Flask, jsonify , render_template
#flask is library and Flask is class

#create flask instance
app = Flask(__name__)

## define function and route
## '/', '/about', '/data'

# @app.route('/')   # base route
# def home():
#     return "Welcome to my website."

@app.route('/about')  # about page route
def about():
    #adding html code down
    return """<h1>About Us</h1><br>
            <h2>PW Skills' vision is to permeate through every student/professionals </h2>
            <h3>Thank You for visiting our website.<h/3>"""
@app.route('/data')   # returns JSON data
def data():
    user_data = {"name": "Abhishek",
                "Age": 21}
    return jsonify(user_data)  # jsonify converts Python dict to JSON

# @app.route('/')
# def home_page():
#     name = "Abhishek"
#     #render_template is the function in the flask used to render/display the html code on to the flask application
#     return render_template('index.html', name=name)

# def home():
# @app.route('/hello')   # extra route instead of duplicate '/'
# def hello():
#     return "Hello World!"


@app.route('/', methods= ['GET'])
def form():
    return render_template("form.html")

@app.route('/form', methods = ['POST'])
def welcome():
    return "We have received your information."

#agr hum yha upar POST ki Jagah GET likh denge toh url mai username aur password show hoga
#So, GET is not secured

## trigger the flask app
if __name__ == '__main__':
    app.run(debug = True)  #debug = True the changes you make will appear in real time
#app is instance and run is function

#http is protocol
#127.0.0.1 is your PC local IP address and 5000 is default port

#base url like google, amazon, etc.
