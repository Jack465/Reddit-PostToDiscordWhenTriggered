# Reddit Send Message to Discord when called on Reddit

This script watches a specific subreddit for it to be called, and when it is, it sends the link to a discord channel via a webhook.

# Requirements
```
pip3 install requests
pip3 install praw
```

# How to use

## Setting up the discord webhook

* First you will navigate to the channel where you want the messages sent to, and then hover over the channel name and click the settings icon

![Discord1](https://i.imgur.com/vLAnu2A.png)

* After that you will press "Integrations" on the menu that shows up, and then click "Webhook", and then click "New Web Hook"

![Discord2](https://i.imgur.com/1WUx5bm.png)

* When you click "New Webhook" you will be prompted to enter a name for the Web Hook, and the channel that you want the messages to be posted in. Select the appropriate options for your server setup. After you have set a name, and channel click the "Copy Webhook URL" Button and then insert that URL in the ```conf.ini``` file at the option ```discord_webhook``` on line 9. 

# Final Setup

1. Generate a client secret and id at https://www.reddit.com/prefs/apps, and copy those into the ```conf.ini``` file on lines 4 and 5
2. Enter your Reddit Account username and password onto ```conf.ini``` lines 2 and 3
3. Set your target subreddit on line 7,
4. Set the name you want your bot to watch for on line 8 (for example set u/yourbotname if you want users to call u/yourbotname)
5. Enter the discord webhook url if you haven't already
6. Enter the name you want your discord bot to display whe it posts the message in the channel. 