Save the configuration in a YAML file, with things like basic intro


Classes:

Note that we will have an overall teacher class that will be inhereted by classes and we define the send message and deploy there - but all the other logic is done in the teacher class

Feel a bit weird but want all the platforms to have the same structure of class but not sure how to do - as function names etc. should be the same, but the contents different

## Streaming
The key is to make a class that inherits the tweepy.StreamListener class - and define an `on_status` function => This is called a LISTENER

Then we open a STREAM, using our API and LISTENER

Then this stream follows something, defined by by a few functions

We should send a message depending on the "on_status" or general data retrieval - not sure exactly where it enters
= seems like on_direct_message with userstream() instead of filter() > as it accesses own
= NOTE that must allow permissions for direct messages

https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py

So should build up the class to do this

NOTE that userstream is gone - need to filter - i guess could filter for users that are following?

Filter is only for tweets so to do it messagewise, must list messages and refresh
- What we could do is take tweets and delete them, which would delete them for us but not for them - this would stop us needing to keep a log