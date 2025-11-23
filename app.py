from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():
    username = request.args.get("name")
    conn = sqlite3.connect("users.db")
    
    # ❌ Vulnerable SQL Injection
    query = "SELECT * FROM users WHERE name = '%s'" % username
    result = conn.execute(query).fetchall()
    
    return str(result)

app.run()
