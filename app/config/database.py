import os

# NOTE that these need to match up with the argument name for tweepy - not ideal but whatevs
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')

# Save in dictionary for easy access
required = ['DB_NAME']
config = {'required' : {}, 'optional' : {}}
config['required'] = {var.split('_')[1].lower() : locals()[var] for var in required}
config['optional'] = {
    var.split('_')[1].lower() : locals()[var] for var in locals().keys() if (
        var[:2] != '__' and var[-2:] != '__' and var not in required
    )
}