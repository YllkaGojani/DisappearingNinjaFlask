from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
colors = {'red':'raphael.jpg', 'orange':'michelangelo.jpg', 'blue':'leonardo.jpg', 'purple':'donatello.jpg', 'april': 'notapril.jpg'}

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja')
def ninjas():
	data = colors
	data.pop('april')
	contents = colors
	return render_template("ninja.html",contents = data)

@app.route('/ninja/<color>')
def color(color):
	data = {}
	if color == 'red' or color == 'blue' or color == 'purple' or color == 'orange':
		data[color] = colors[color]
	else:
		data['april'] = colors['april']
	return render_template("index.html",contents = data)

if __name__ == "__main__":
	app.run(debug=True)	