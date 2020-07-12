import json
import datetime

import tweepy

class BasicStreamListener(tweepy.StreamListener):
    def on_direct_message(self, status):
        print('Received message: ', status)
    
    def on_error(self, status_code):
        print('Error! ', status_code)
        return False

if __name__ == '__main__':

    with open('bot-creds.creds') as json_file:
        credentials = json.load(json_file)
    
    auth = tweepy.OAuthHandler(credentials['api']['key'], credentials['api']['secret'])
    auth.set_access_token(credentials['access']['token'], credentials['access']['secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    print(api.list_direct_messages()[0])
    print(api.list_direct_messages()[0].created_timestamp)
    print(datetime.datetime.fromtimestamp(int(api.list_direct_messages()[0].created_timestamp)/ 1000))
    print(datetime.datetime.fromtimestamp(int(api.list_direct_messages()[1].created_timestamp)/ 1000))
    print(datetime.datetime.fromtimestamp(int(api.list_direct_messages()[2].created_timestamp)/ 1000))
    print(api.list_direct_messages()[0].message_create['sender_id'])

    for i in range(10):
        print(i+1)
        api.send_direct_message('56980092', f'Trial {i}')