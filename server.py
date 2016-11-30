from flask import Flask, jsonify, redirect, url_for, request
app = Flask(__name__)

@app.route('/pages/<PageName>/')
def LoadPage(PageName):
	return app.send_static_file('pages/' + PageName +'.html')

@app.route('/')
def index():
	return redirect(url_for('LoadPage', PageName = 'Login'))

@app.route('/UserVerify/', methods=['POST'])
def UserVerify():
	# print(request.headers)
	# print(request.form.get('ID'))
	userID = request.form.get('ID')
	passwd = request.form.get('password')
	if len(userID) <= 2:
		identity = 'A'
	elif len(userID) <= 4:
		identity = 'T'
	elif len(userID) <= 6:
		identity = 'S'
	else:
		identity = 'V'


	if userID == passwd:
		result = "Y"
	else:
		result = "N"

	return jsonify({'result': result, 'Identity': identity, "Name": "Nemo"})

if __name__ == '__main__':
    app.run(debug=True)