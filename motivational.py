#A script to analyze Reddit's Get Motivated subreddit
import praw #This is Reddit's API
import nltk

#We need to set the user_agent for Reddit
user_agent = ("Motivational sayings 1.0 by /u/DistrictRails")
r = praw.Reddit(user_agent=user_agent)

#Obtain the comments from GetMotivated
subreddit = r.get_subreddit('getmotivated')
subreddit_comments = subreddit.get_comments()

tokens = nltk.word_tokenize(subreddit_comments)
#for i in subreddit_comments:
#    print i

