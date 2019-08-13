# Twitter bot series - followers bot

Followers bot is very simple. It gets your current followers count, and updates a database table with the information.

## Dependencies - what to install

This bot uses the following third party modules:

- tweepy (for access to Twitter api)
- psycopg2 (for interaction with postgresql)

Install these with pip in your virtual environment or globally. To learn how to work in virtual environments with python, you can read my [blog post here.](https://medium.com/@janelgbrandon/setting-up-a-python-development-environment-2e18447cbc24)

## Dependencies - database and enviroment variables

### Database requirements

This bot uses a postgresql db instance. It assumes that the following environment variables are exported (see db_connect.py):

- DBUSER (your postgresql user name)
- DBPW (your postgresql password)
- TWITTERDB (the database you are using for this bot)

This assumes you have a postgresql server instance running on port 5432 on localhost. You will have to modify the db_connect.py if you are using a non-default port or an external server.

You can create a database in your postgresql instance with a simple CREATE DATABASE command. You will have to do this before you use this bot, and specify the database name for the TWITTERDB environment variable. You can use an existing database if desired. I've created a database for all of my twitter bots called "twitterbot_dev", but you can do as you please.

### Authorization requirements

This bot authenticates with Twitter, and requires that you have a [developer account](https://developer.twitter.com/en/apply-for-access.html)

The bot assumes the following environment variables are set for authentication (see twitter_auth.py module). These values will be shown when you apply for a developer account, or when you view your developer account information in Twitter (at developer.twitter.com):

- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET
- TWITTER_ACCESS_TOKEN_KEY
- TWITTER_ACCESS_TOKEN_SECRET

## Setting up the database

The create_db.py module is included to create the 'follower_counts' table. This table will store an auto-incrementing id (id), the number of followers (count), and the date the record is created (created_at).

Run `python create_db.py` once to create the table before you run the bot.

## Running the bot

Run the bot with `python follower_count.py`
It will print messages to show connection and disconnect from the database, and the count updated in the table.
