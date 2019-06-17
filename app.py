import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

count = 0 
	
@app.route('/', methods=['GET'])
def index():
	url_parse = request.url
	if 'return' in url_parse:
		return "OK"
	elif 'solve' in url_parse:
		return "Will solve in a second..."
	elif 'hear' in url_parse:
		return "Jenny Gasparis"
	elif 'email' in url_parse:
		return "cohenss@vcu.edu"
	elif 'years' in url_parse:
		return "1"
	elif 'position' in url_parse:
		return "Data Engineer / Data Pipeline Developer at EMX Digital"
	elif 'degree' in url_parse:
		return "Applied Mathematics"
	elif 'resume' in url_parse:
		return "<github link here>"
	elif 'name' in url_parse:
		return "Scott Cohen"
	elif 'phone' in url_parse:
		return "804-399-9345"
	elif 'source' in url_parse:
		return "<github link here>"
		


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
