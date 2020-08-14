import os

### Messages ###
M_INTRODUCTION = "Hello! I am the teacher bot and I want to help you master data science. What do you want to do?"
M_NOARTICLE = "Sorry, no more articles for today!"
M_HELP = "I am the teacher bot and I'm here to help you master data science, to interact with me send any of the following messages:\nHelp: Ask for help\nSend me an article: Ask for an article"
M_NOTFOUND = "Sorry, I don't understand what you mean - you can ask for help by sending 'help'"

### Interactions ###
I_ARTICLE = "send me an article"
I_HELP = "help"

# Save in dictionary for easy access
config = {'responses' : {}, 'user_options' : {}}
config['responses'] = {
    var.split('_')[1] : locals()[var] for var in locals().keys() if var[:2] == 'M_'
}

# For the user options, we do the opposite due to look up - these will be sent as the "options" for the get_reply function
config['user_options'] = {
    locals()[var] : var.split('_')[1] for var in locals().keys() if var[:2] == 'I_'
}