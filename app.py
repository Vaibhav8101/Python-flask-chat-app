# from flask import Flask,jsonify,request

# app=Flask(__name__)#creating app that is __main__
# @app.route('/')  #calling root page  and /hello for not a home page if we use /hello then error shown resolve by using localhost
# def hello():#defining function
# 	return "hello"
# if __name__=="__main__":#it return only when main function encounter
# 	app.run()
# users=[
# {'id':2,'name':'Anne','age':20},
# {'id':1,'name':'cathy','age':21},
# {'id':3,'name':'Bill','age':19}
# ]
# app=Flask(__name__)#creating app that is __main__
# @app.route('/')  #calling root page  and /hello for not a home page if we use /hello then error shown resolve by using localhost
# def hello():#defining function
# 	return "hello"
# @app.route('/users')
# def getUsers():
# 	return jsonify(users)#json is used to return string format because browser does not understand python list format
# if __name__=="__main__":#it return only when main function encounter
# 	app.run()
# app=Flask(__name__)	

# users=[
# {'id':2,'name':'Anne','age':20},
# {'id':1,'name':'cathy','age':21},
# {'id':3,'name':'Bill','age':19}
# ]
# @app.route('/users')
# def getUsers():
# 	return jsonify(users)
# @app.route('/users/<id>')#when we put in bracket this mean it is variable
# def getUser(id):
# 	# result=[u for u in users if u['id']==id]
# 	result=list(filter(lambda u: str(u['id'])==id,users))#converting int into string
# 	return jsonify(result)

# if __name__=="__main__":#it return only when main function encounter
# 	app.run()	
# app=Flask(__name__)	

# users=[
# {'id':2,'name':'Anne','age':20},
# {'id':1,'name':'cathy','age':21},
# {'id':3,'name':'Bill','age':19}
# ]
# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')
# @app.route('/users')
# def getUsers():
# 	print(users)
# 	return jsonify(users)
# @app.route('/users/<id>')#when we put in bracket this mean it is variable
# def getUser(id):
# 	# result=[u for u in users if u['id']==id]
# 	result=list(filter(lambda u: str(u['id'])==id,users))#converting int into string
# 	return jsonify(result)

# if __name__=="__main__":#it return only when main function encounter
# 	app.run()



from flask import Flask,jsonify,request
from flask_socketio import SocketIO
app=Flask(__name__)
app.config['SECRET_KEY']='codingelement'
socketio=SocketIO(app)
# app=Flask(__name__)
users=[
{'id':2,'name':'Anne','age':20},
{'id':1,'name':'cathy','age':21},
{'id':3,'name':'Bill','age':19}
]
@app.route('/')
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handle_msg(data):
	socketio.emit('push',data,broadcast=True,include_self=False)


@app.route('/users')
def getUsers():
	print(users)
	return jsonify(users)
@app.route('/users/<id>')#when we put in bracket this mean it is variable
def getUser(id):
	# result=[u for u in users if u['id']==id]
	result=list(filter(lambda u: str(u['id'])==id,users))#converting int into string
	return jsonify(result)

if __name__=="__main__":#it return only when main function encounter
	socketio.run(app)