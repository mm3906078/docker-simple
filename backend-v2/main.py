#!/usr/bin/env python

import os
import json
from flask import Flask, request, jsonify
import mysql.connector

db = mysql.connector.connect(
  host = os.getenv('host'),
  user = os.getenv('user'),
  passwd = os.getenv('passwd'),
  database = os.getenv('database')
)

app = Flask(__name__)

def initialize(dbcon):
    cursorObject = dbcon.cursor()

    studentRecord = """CREATE TABLE DATA (
                   NAME  VARCHAR(20) NOT NULL,
                   EMAIL VARCHAR(50)
                   )"""

    if (checkTableExists(dbcon,"DATA") == False):
        cursorObject.execute(studentRecord)
    dbcon.close()

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    db.reconnect()
    cursorObject = db.cursor(buffered=True)
    cursorObject.execute(f"SELECT * FROM DATA WHERE NAME = '{name}'")
    res = cursorObject.fetchall()
    if res != []:
        return jsonify(res), 200
    else:
        return jsonify({'error': 'data not found'}), 404

@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    db.reconnect()
    cursorObject = db.cursor(buffered=True)
    cursorObject.execute("SELECT * FROM DATA")
    res = cursorObject.fetchall()
    recordt = (record['name'],record['email'])
    if recordt not in res:
        cursorObject.execute("INSERT INTO DATA VALUES(%s, %s)",(record['name'],record['email']))
        db.commit()
        db.close()
    return jsonify(record), 200

@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    db.reconnect()
    cursorObject = db.cursor(buffered=True)
    cursorObject.execute("SELECT * FROM DATA")
    res = cursorObject.fetchall()
    recordt = (record['name'],record['email'])
    if recordt in res:
        cursorObject.execute(f"DELETE FROM DATA WHERE NAME = '{record['name']}'")
        db.commit()
    return jsonify(record), 200

if __name__ == "__main__":
    initialize(db)
    app.run(host="0.0.0.0", port=8000, debug=True)
