from flask import Flask, request, jsonify, send_file
import os
import re


app = Flask(__name__)
match_path = '/media/ignacio/f0af6c7b-75a8-42ad-b314-6802b01b0ad91/home/ayhon/ignacio/Event Catcher/full matches'

@app.route("/get-user/<user_id>")
def get_user(user_id):
	user_data = {
	"user_id":user_id,
	"name":"Ignacio Leal",
	"email":"ignacioleal000@gamil.com"}
	
	extra = request.args.get("extra")
	if extra:
		user_data["extra"] = extra
	
	return jsonify(user_data), 200

@app.route("/matches/list")
def send_match_list():
	matches = os.listdir(match_path)
	response = {}
	for match in matches:
		# Extract match teams
		match_pattern = re.search(r'(\w+)\.v\.(\w+)', match).group()
		# Extract league
		league_pattern = re.search(r'\.\d+\.(\w+)\.', match).group()
		# Extract date
		date_pattern = re.search(r'\d{2}\.\d{2}\.\d{4}', match).group()
		response[match_pattern] = [league_pattern, date_pattern]
	return response
		
@app.route("/matches/<match_id>")
def get_matches_id(match_id):
	path = match_path+"/"+match_id+'/'
	files = os.listdir(match_path+"/"+match_id)
	for file in files:
		try:
			return send_file(path+file, as_attachment=True)
		except FileNotFoundError:
			return jsonify({"error": "File not found"}), 404
	
if __name__ == "__main__":
	app.run(debug=True,host = "192.168.1.44")
