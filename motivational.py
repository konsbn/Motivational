#Comments
import praw

user_agent = ("Motivational sayings 1.0 by /u/DistrictRails")
r = praw.Reddit(user_agent=user_agent)

subreddit = r.get_subreddit('getmotivated')
subreddit_comments = subreddit.get_comments()
for i in subreddit_comments:
    print i
