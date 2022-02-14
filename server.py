from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list')
def list():
    users = [
    {'first_name' : 'Alberto', 'last_name' : 'Ibarra'},
    {'first_name' : 'Dylan', 'last_name' : 'Ibarra'},
    {'first_name' : 'Mattix', 'last_name' : 'Garcia'},
    {'first_name' : 'Melissa', 'last_name' : 'Ibarra'}
]
    return render_template("index.html", users=users)


if __name__=="__main__":



    app.run(debug=True)