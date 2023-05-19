from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html") #render_template class is used to load html from another folder

if(__name__== '__main__'):
    app.run(debug=True)
  