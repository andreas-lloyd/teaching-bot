# Teaching bot
A bot that will recommend **high quality** data science content to users and learn what sort of preferences they have.

## General technical layout (DRAFT)
The general layout of the app is as follows:

1. The database is created by running `database/create_database.py`
2. The bot for each platform is contained in `bot/platforms/...`
    * In each one of the platforms there is a `run_bot.py` script that is used to launch the bot to listen
    * Each folder also contains the appropriate Docker file that builds the image used to actually deploy the bot
3. Each platform specific script leans on the `bot/teacher.py` script that defines the basic logic for all the bots
    * The platform specific scripts only provide a translation layer to interact with this
    * They also provide the specific way to deploy the bot to "listen"