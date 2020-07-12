"""
Note that need to understand how to close stream - there might be a bit where have to do 'WITH STREAM' or something,
otherwise stream.disconnect() which is activated on next playthrough of stream
"""
import time

import tweepy

from teacher import Teacher


class TwitterBot(Teacher):
    """The bot that will be launched on Twitter. This originally worked trying to stream
    direct messages, but since userstream has been depreciated, this won't be possible anymore
    unless we move to do it Tweet based, which would probably be more complicated as would
    need to track replies and stuff.
    """
    def __init__(self, credentials, bot_config):
        super().__init__(bot_config)

        # Initiate the API
        self.create_api(credentials)

        # Get own user id
        self.user_id = self.api.me().id

    def create_api(self, credentials):
        """Wrap up the creation of the API that we will exploit."""
        auth = tweepy.OAuthHandler(
            credentials['api']['key'], credentials['api']['secret']
        )

        auth.set_access_token(
            credentials['access']['token'], credentials['access']['secret']
        )

        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    def send_message(self, destination, out_message):
        """A wrapper to send a message with error handling."""
        if out_message[0] != 'ERROR':
            self.api.send_direct_message(destination, out_message[1])
        else:
            self.log_error(out_message[0])

    def stream_messages(self, refresh_rate=60, message_wait=10, delete_wait=10):
        """Our dumb way of streaming messages which will consist in loading our messages
        every 60 seconds (default), processing each message, and deleting them once we have processed
        them.
        """
        while True:
            messages = self.api.list_direct_messages()
            print(f'Processing {len(messages)} messages')

            pending_messages = {}
            message_ids = []
            for message in messages:
                sender = message.message_create['sender_id']
                inc_message = message.message_create['message_data']['text']

                # Messages come in time order so just save the first to reply to it
                if sender not in pending_messages and sender != self.user_id:
                    pending_messages[sender] = inc_message
                
                # We want to delete all messages
                message_ids.append(message.id)
            
            for user_id in pending_messages:
                self.send_message(sender, self.process_message(user_id, pending_messages[user_id]))
                time.sleep(message_wait)

            for message in message_ids:
                self.api.destroy_direct_message(message)
                time.sleep(delete_wait)

            time.sleep(refresh_rate)