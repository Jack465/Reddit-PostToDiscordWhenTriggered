import praw
import requests
import os
import sys
import configparser
import re
import json

config = configparser.RawConfigParser()
config.read('conf.ini')

reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']

targetSubreddit = config['VARI']['target_subreddit']
botName = config['VARI']['bot_name']
discordWebhook = config['VARI']['discord_webhook']
discordSendAs = config['VARI']['discord_send_as']

waiting_list = []
if os.path.isfile('processed_comments.txt'):
	with open('processed_comments.txt','r') as file:
		processed_comments = [line.rstrip('\n') for line in file]

def main():
	reddit = praw.Reddit(client_id=reddit_client_id,
					client_secret=reddit_client_secret,
					user_agent="python:send reddit post to discord server:v1 (by u/throwaway176535)",
					username=reddit_user,
					password=reddit_pass)
	for comment in reddit.subreddit(targetSubreddit).stream.comments():
		if re.search(r'\b' + botName + r'\b', comment.body) and comment.link_id not in waiting_list and comment.link_id not in processed_comments:
			print(f"Found submission {comment.link_id}")
			notify("https://reddit.com" + comment.submission.permalink)
			waiting_list.append(comment.link_id)

def notify(message):
	data = {}
	data["content"] = message
	data["username"] = discordSendAs

	output = requests.post(discordWebhook, data=json.dumps(data), headers={"Content-Type": "application/json"})
	try:
		output.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print("Successful in sending")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\n\nStopping script - writing data to text file")
		with open('processed_comments.txt', 'a') as file:
			for item in waiting_list:
				file.write('{}\n'.format(item))
		sys.exit(0)

