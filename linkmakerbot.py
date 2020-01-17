#!/usr/bin/python
import praw
import pdb
import re
import os
import time

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('xkcd')
for submission in subreddit.hot(limit=1):
    #time.sleep(2)
    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:
        # Do a case insensitive search
        temp = re.findall(r'xkcd \d+', submission.title, flags=re.IGNORECASE)
        res = list(temp)
        if len(res)!=0:
            myreply=""
            if len(res)>1:
                myreply="Let me make those links for you:"
            else:
                myreply="Let me make that link for you:"
            for linkNum in res:
                temp = linkNum.split()
                temp = temp[-1]
                temp = int(temp)
                myreply+="\n\nhttps://xkcd.com/%d" %temp
            #print(myreply)
            # Reply to the post
            submission.reply(myreply)
            tempMessage="Bot replying to: %s with ID: %s" %(submission.title,submission.id)
            print(tempMessage)
            #print("Waiting so we don't exceed rate limit...")
            posts_replied_to.append(submission.id)
            #time.sleep(31)

    for thisComment in submission.comments:
        #time.sleep(2)
        if thisComment.id not in posts_replied_to:
            temp = re.findall(r'xkcd \d+', thisComment.body, flags=re.IGNORECASE)
            res = list(temp)
            if len(res)!=0:
                myreply=""
                if len(res)>1:
                    myreply="Let me make those links for you:"
                else:
                    myreply="Let me make that link for you:"
                for linkNum in res:
                    temp = linkNum.split()
                    temp = temp[-1]
                    temp = int(temp)
                    myreply+="\n\nhttps://xkcd.com/%d" %temp
                #print(myreply)
                # Reply to the comment
                thisComment.reply(myreply)
                tempMessage="Bot replying to a comment in: %s with ID: %s" %(submission.title,thisComment.id)
                print(tempMessage)
                #print("Waiting so we don't exceed rate limit...")
                posts_replied_to.append(thisComment.id)
                #time.sleep(31)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
