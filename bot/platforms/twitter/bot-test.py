import yaml

from platforms.twitter.twitterbot import TwitterBot

if __name__ == '__main__':
    with open('creds-bot.yaml') as yaml_file:
        credentials = yaml.load(yaml_file, Loader=yaml.FullLoader)

    twitter_bot = TwitterBot(credentials, '../../bot-config.yaml', True)
    
    twitter_bot.stream_messages()

    print('Done!')