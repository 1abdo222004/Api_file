from flask import Flask,jsonify,request
import json
app=Flask(__name__)
with open('data.json', 'r') as file:
	data = json.load(file)
allowed_ids = data['allowed_ids']
@app.route('/up')
def m():
	id=request.args.get('edit')
	if str(id) in allowed_ids:
		return jsonify('Ok 400')
	else:
	  allowed_ids.append(id)
	  data['allowed_ids'] = allowed_ids
	  with open('data.json', 'w') as file:
	  	json.dump(data, file)
	  	return jsonify('Ok 200')
@app.route('/ip')
def pm():
  id=request.args.get('dalt')
  allowed_ids.remove(id)
  data['allowed_ids'] = allowed_ids
  with open('data.json', 'w') as file:
   json.dump(data, file)
app.run()
