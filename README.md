# Linkmaker Bot for Reddit
This python script is a simple bot for detecting a string in a post or comment, and replies with a link based on that string.

## Installation
- Ensure python and pip are installed.
- Run pip install praw
- Clone the repository
- Modify praw.ini to your Reddit settings

## Running
Run pyton linkmakerbot.py

## Reccomendations
Add a cron job to run the script regularly.

## To Do
- Add error handling
- Make it easier to customize the subreddit and the search string
- Code cleaning

## Notes
Praw should regulate how frequently requests are made so you don't exceed the limit set by Reddit.  However, it is different depending on the account age and karma.  Therefore, it may take time for this script to be useful on a new account.

Also, this script was hacked together in about 10 mins, and is by no means professional.  Recommend modifications and use this as a quick base.

This code is based on the work found at https://github.com/shantnu/RedditBot/
