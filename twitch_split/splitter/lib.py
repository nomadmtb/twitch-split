import requests

def validate_streams(param_usernames):
	streams = {}
	for username in param_usernames:
		r = requests.get('https://api.twitch.tv/kraken/streams/' + username, headers={"Accept": "application/vnd.twitchtv.v3+json"})
		streams[username] = r.json
	return streams
