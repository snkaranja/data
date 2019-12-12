from app import app
from flask import jsonify, request, render_template
		
@app.route('/')
def Dashboard():
	return render_template('dashboard.html')
