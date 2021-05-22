'''from flask import Flask, render_template

app = Flask(__name__,template_folder='Layihe')

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/ilkin")
def ilkin():
  return render_template('ilkin.html')

@app.route("/subhan", methods=['GET','POST'])
def subhan():
  return render_template('subhan.html')
        
if __name__=='__main__': 
  app.run(debug=True)'''






from flask.app import Flask


app=Flask

@app.route("route")
def func():