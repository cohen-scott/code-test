import os
from flask import Flask,  request, redirect, url_for, jsonify
import random as rn
from werkzeug import CombinedMultiDict, ImmutableMultiDict

app = Flask(__name__)

def getUniqueValues(conditional_list):
     
	conditionals = [w.replace('=', '==') for w in conditional_list]

	A = rn.randint(1,10)
	B = rn.randint(1,10)
	C = rn.randint(1,10)
	D = rn.randint(1,10)

	while not ((eval(conditionals[0])) and (eval(conditionals[1])) and (eval(conditionals[2])) and (eval(conditionals[3]))):
		A = rn.randint(1,10)
		B = rn.randint(1,10)
		C = rn.randint(1,10)
		D = rn.randint(1,10) 

	return {"A": A, "B": B, "C": C, "D": D}
 

def getConditionals(facts, values):
     
	conditionals = []
	for i in range(0, len(facts)):

		value_text = values[i]
		
		split_text = list(facts[i].split(value_text)[1])
		print(split_text)
		
		for v in range(0, len(split_text)):
			if not '-' in split_text[v]:
				conditionals.append('{}{}{}'.format(value_text, split_text[v], values[v])) 
			
	return conditionals
 
def getAnswer(facts, values, answer):   
	stuff = []
	for i in range(0, len(facts)):


		value_text = values[i]
		split_text = list(facts[i])

		for j in range(0, len(facts)):

			if split_text[j+1] == '-':

				if answer[value_text] == answer[values[j]]:
					statement = '='
					split_text[j+1] = split_text[j+1].replace('-', '{}'.format(statement))
					
				elif answer[value_text] > answer[values[j]]:
					statement = '>'
					split_text[j+1] = split_text[j+1].replace('-', '{}'.format(statement)) 
					
				elif answer[value_text] < answer[values[j]]:
					statement = '<'
					split_text[j+1] = split_text[j+1].replace('-', '{}'.format(statement))   

		stuff.append(split_text)
		
	return stuff
	
@app.route('/', methods=['GET'])
def index():

	final_answer = []

	url_parse = request.url
	if 'return' in url_parse:
		return "OK"
	elif 'solve' in url_parse:
		
		immutable_object = request.values
		string = list(list(immutable_object.items())[1])
		facts = string[1].split(' ')[4].replace("\n", ' ').split()[1:]
		print(facts)
		
		values = string[1].split(' ')[4].replace("\n", ' ').split()[0]
		values = (list(item) for item in values.split())
		values = list(values)[0]
		print(values)
		
		
		conditionals = getConditionals(facts, values)
		print(conditionals)
		answer = getUniqueValues(conditionals)
		print(answer)
		answer = getAnswer(facts, values, answer)
		
		for i in answer:
			i[1:5] = [''.join(i[1:5])]
			
			new_stuff = ''.join(i) + '\n'
			final_answer.append(new_stuff)
			
			s = " ABCD\n"
			for i in final_answer:
				s += i
		return s
		
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
	elif 'cover' in url_parse:
		return "https://github.com/cohen-scott/resume"
	elif 'name' in url_parse:
		return "Scott Cohen"
	elif 'phone' in url_parse:
		return "804-399-9345"
	elif 'submission' in url_parse:
		return "https://github.com/cohen-scott/code-test"
	elif 'eligibility' in url_parse:
		return "Yes"
	
	return ""

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
