from flask import Flask 
app = Flask(__name__)
@app.route("/")
def hello():
    return "learning concepts is easy   in devops but applying,debuging is what a real task is !!!!!! and its a task to become better every day with consistency "
if __name__ == "__main__":
    app.run(host = "0.0.0.0" ,port= 5000)
