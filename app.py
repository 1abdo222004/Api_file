from flask import Flask,jsonify,request
from requests import *
url ="https://zvypfaqwfvfebolunupf.supabase.co/rest/v1/groups?select=id&apikey=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2eXBmYXF3ZnZmZWJvbHVudXBmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM0OTY3NTAsImV4cCI6MjAzOTA3Mjc1MH0.BMGw4C1rks6AdPxv7MsB7lpt2D3-ARywplmpwh-0zRo"
app=Flask(__name__)
@app.route('/')
def m():
	id=[]
	ids=get(url).json()
	for idx in range(len(ids)):
		p = ids[idx]['id']
		id.append(p)
	return id

app.run(host="0.0.0.0", port=8080)
