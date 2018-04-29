from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os.path


app = Flask(__name__)
CORS(app)

sqlite_file = 'users1.db'#/Users/Sebastian/Desktop/'

conn = sqlite3.connect(sqlite_file,check_same_thread=False)
#print(conn)

sqlite_file2 = 'CLIENT1.db'#/Users/Sebastian/Desktop/'
conn2 = sqlite3.connect(sqlite_file2,check_same_thread=False)




c = conn.cursor()
c2 = conn2.cursor()


def create_table():
	#c = conn.cursor()
	#c.execute('DROP TABLE USERS')
	c.execute('CREATE TABLE IF NOT EXISTS USERS1(NAME text, password text )')
	c2.execute('CREATE TABLE IF NOT EXISTS CLIENT1(NAME text, Address text, Phone Integer)')
	#print(c)
	conn.commit()
	conn2.commit()


create_table()



@app.route('/a', methods=['POST'])
def login():
	res =0 
	c = conn.cursor()
	data = request.get_json()
	fn = data['firstname']
	#print("Username is ",fn)
	ps = data['password']
	#print("PAssword is ",ps)
	c.execute("SELECT * from USERS1 WHERE NAME = ?", (fn,))
	data = c.fetchall()
	if len(data) !=0:
		user = data[0][0]
		password = data[0][1]
		print(user)
		print(password)
		print("testing")

		if user==fn and password==ps:
			res = 2 #when user is  exists and password is same
		elif password!=ps:
			res =1 #when user does not exist
		elif user!=fn:
			res = 0 #user does not exist
	else:
		if len(fn)==0 or len(ps) ==0:
			res = 500
		else:
			res = 10

	print(res)
	conn.commit()
	return jsonify(res)


@app.route('/b', methods=['POST'])
def newuser():
	c = conn.cursor()
	data = request.get_json()
	fn = data['firstname']
	ps1 = data['password1']
	ps2 = data['password2']
	c.execute("SELECT * from USERS1 WHERE NAME = ?", (fn,))
	data1 = c.fetchall()
	res = -1
	print(data)
	if len(fn) == 0 or len(ps1) ==0 or len(ps2)==0:
		print("aa")
		res =500 # no username or password given
		return jsonify(res)
	elif ps1!=ps2:
		res =1
		print("b")
		return jsonify(res)#Password is not same

	#user name and password is given
	if len(data1) ==0:
		print(data1)
		c.execute("INSERT INTO USERS1(name,password) VALUES(?,?) ", (fn,ps1))
		conn.commit()
		res =10
		return jsonify(res)
	else:
		res = 0
		c.execute("SELECT * from USERS1")
		data = c.fetchall()
		print(data)
		return jsonify(res)

	
	return jsonify(res)



@app.route('/c', methods=['POST'])
def profile():
	res =1
	c2 = conn2.cursor()
	print(c2)
	data = request.get_json()
	print(data)
	fn = data['name']
	ad = data['Address']
	ph = data['Phone']
	

	c2.execute("SELECT Phone from CLIENT1 WHERE Phone = ?", (ph,))
	data = c2.fetchall()
	if len(data)==0:
		c2.execute("INSERT INTO CLIENT1(NAME,Address,Phone) VALUES(?,?,?) ", (fn,ad,ph))
		res =0
		conn2.commit()
	
	return jsonify(res)



	

app.run(debug=True)
