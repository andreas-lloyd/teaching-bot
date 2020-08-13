# Postgres
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
sudo -i -u postgres
createuser ubuntu -P --interactive
createdb test

# PeeWee
sudo apt update
sudo apt install python3-pip
sudo pip3 install Psycopg2 # NOT SURE
sudo pip3 install peewee

# Build tables
db = peewee.PostgresqlDatabase('test', user='ubuntu') # Note don't supply host because no password

Then just build like normal - nothing more complicated

Pre-packaged: https://aws.amazon.com/getting-started/tutorials/create-connect-postgresql-db/

https://www.shubhamdipt.com/blog/postgresql-on-ec2-ubuntu-in-aws/
- Need to edit two configuration files to allow inbound traffic, as well as allow Custom TCP: 5432