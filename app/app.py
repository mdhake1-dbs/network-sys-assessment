from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from the automated container! Test by Ubuntu User Welcome to Ireland Shreyas"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

