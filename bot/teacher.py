import yaml


class Teacher():
    """The base class that we will use to define the most basic logic of the bot, and will be common to all platforms.
    This class will handle all the backend elements and tell the bot want to respond. All of the logic for
    receiving and sending messages will then be defined in the specific API of that bot.
    """
    def __init__(self, bot_config):
        with open(bot_config) as yaml_file:
            self.bot_options = yaml.load(yaml_file, Loader=yaml.FullLoader)
    
    def log_error(self, error):
        print(error)

    def is_first(self, user_id):
        return True

    def get_reply(self, option):
        """Get the message that we want to send."""
        if option == 'introduction':
            return ('SUCCESS', self.bot_options['messages']['introduction'])
        elif option == 'not found':
            return ('SUCCESS', self.bot_options['messages']['not_found'])
        else:
            return ('ERROR', 'No message related to the specified option') 

    def process_message(self, user_id, inc_message):
        """Take the incoming message and according to the logic provide the get_reply function with the right arguments.
        Note that everything that comes in should be responded to in some way (i.e. we always give feedback to the user),
        which is why everything returns the `get_reply` function, but the backend aspects are all dealt with here.
        """
        # The first thing to do is to check if they asked for any of our options
        if inc_message not in self.bot_options['interaction']['user_options'].values():
            # Now check if this is the first message we send to them - otherwise ask for help
            if self.is_first(user_id):
                return self.get_reply('introduction')
            else:
                return self.get_reply('not found')
        else:
            return self.get_reply(self.bot_options['interaction']['user_options'][inc_message])