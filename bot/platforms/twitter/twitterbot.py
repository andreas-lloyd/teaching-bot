"""
Note that need to understand how to close stream - there might be a bit where have to do 'WITH STREAM' or something,
otherwise stream.disconnect() which is activated on next playthrough of stream
"""
import tweepy

from teacher import Teacher


class TwitterBot(Teacher):
    """The bot that will be launched on Twitter. This originally worked trying to stream
    direct messages, but since userstream has been depreciated, this won't be possible anymore
    unless we move to do it Tweet based, which would probably be more complicated as would
    need to track replies and stuff.
    """
    def __init__(self, credentials):
        # Initiate the API
        self.create_api(credentials)

        # Initiate the stream
        self.create_stream()

    def create_api(self, credentials):
        """Wrap up the creation of the API that we will exploit."""
        auth = tweepy.OAuthHandler(
            credentials['api']['key'], credentials['api']['secret']
        )

        auth.set_access_token(
            credentials['access']['token'], credentials['access']['secret']
        )

        self.api = tweepy.API(auth)
    
    def create_stream(self):
        """
        To active this to listen we need to create a stream that defines how to take in messages.
        """
        class MessageStreamListener(tweepy.StreamListener):
            def on_direct_message(self, status):
                """
                This function defines how we respond to a direct message, where
                we process the status text to decide what to do 
                """
                print('Received message')
                response = self.process_message(status.text)

                self.send_message(response, status.user_id)
        
        # We define the listener and then active the stream
        self.stream_listener = MessageStreamListener()
        self.message_stream = tweepy.Stream(auth=self.api.auth, listener=self.stream_listener)

    def start_stream(self):
        """Using what we defined to create the stream we active it here and get running"""
        self.message_stream.userstream()

    def send_message(self, destination, out_message):
        """A wrapper to send a message with error handling."""
        if message[0] != 'ERROR':
            self.api.send_direct_message(destination, out_message[1])
        else:
            self.log_error(out_message[0])