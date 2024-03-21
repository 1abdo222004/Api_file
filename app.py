from flask import Flask,jsonify,request
from requests import *
url ="https://idwyvctdeopxpsomnrmy.supabase.co/rest/v1/admin?select=id&apikey=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlkd3l2Y3RkZW9weHBzb21ucm15Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA4NzUzNTYsImV4cCI6MjAyNjQ1MTM1Nn0.90KRZaat7FuXBIsjuYOiT1-2VmtkdAQwM6pkKt6ZwK0"
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
