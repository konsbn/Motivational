#A script to analyze Reddit's Get Motivated subreddit
#Still in the works but getting there...
import praw #This is Reddit's API
import json
import os

#We need to set the user_agent for Reddit
user_agent = ("Motivational sayings 1.0 by /u/DistrictRails")
r = praw.Reddit(user_agent=user_agent)
#Obtain the comments from GetMotivated
subreddit = r.get_subreddit('getmotivated')
comments = subreddit.get_comments()
#flat_comments = praw.helpers.flatten_tree(comments)


f = open('output.txt', 'w')
words = {}
for comment in comments:
    for word in comment.body.split(" "):
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 0
    print(json.dumps(words, f))
    words.clear()
    f.flush()
f.close()

'''
file_name = "data_dump"
with open(file_name, 'w') as outfile:
    json.dump(data, outfile)
    print "Page {}".format(i+1:)


fo = open('foo.txt', "rw+")
print "Name of the file: ", fo.name



src = StringIO()
p = pickle.Pickler(src)
p.dump(comments)
'''
