import json

from platforms.twitter.twitterbot import TwitterBot

if __name__ == '__main__':
    with open('bot-creds.creds') as json_file:
        credentials = json.load(json_file)

    twitter_bot = TwitterBot(credentials)
    
    while True:
        twitter_bot.start_stream()

    print('Done!')