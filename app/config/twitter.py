import os

API_KEY = os.environ.get('TWITTER_API_KEY')
API_SECRET = os.environ.get('TWITTER_API_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')

# Save in dictionary for easy access
config = {var : locals()[var] for var in locals().keys() if var[:2] != '__' and var[-2:] != '__'}