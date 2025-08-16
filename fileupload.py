#File Upload HAndling in flask
from flask import Flask , render_template , request
#render_template → lets you load HTML files.
#request → lets you access form data, files, query params, etc.

app = Flask(__name__)  #You are creating an instance of the Flask class.
#__name__ :- tells Flask where to find resources like templates and static files

#define your endpoints here
@app.route('/', methods = ['GET'])
def home():
    return render_template('form2.html')
#loads and returns the html form

@app.route('/upload', methods=['POST'])
def get_data():
    
    
    file = request.files['file'] #file is variable
    #Gets the uploaded file object from the form (in Postman or HTML, the field name must be file).
    
    
    print("this is what it contains: ",request.files)
    print("file:" ,file)
    #print all uploaded files and specifically the one in file variable.
    
    if file.filename.endswith('.csv'):
        path = "userfile/" + file.filename
        file.save(path)
        return "We have recived your file"
    else:
        return "Upload a CSV file only."
    
    

if __name__ =='__main__': #This part makes sure your app runs only when you run this file directly, not when you import it from somewhere else.
    app.run(debug=True)  #starts a development web server