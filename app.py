from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username", "")
    password = data.get("password", "")
    
    if password == "2431":
        # simulate loading time
        time.sleep(3)
        return jsonify(success=True, message=f"Access granted. Welcome, {username}.")
    else:
        return jsonify(success=False, message="Access denied. Incorrect password.")

if __name__ == "__main__":
    app.run(debug=True)