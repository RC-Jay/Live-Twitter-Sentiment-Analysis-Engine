# README #

This software helps you graph out sentiments on data streamed live from twitter on any topic. The sentiment analysis engine is built by training data from the url mentioned below. It's just a bunch of short reviews which have been tagged as positive and negative. Also I have used a bunch of classifiers to get the sentiment on any text and finally choose a mode of all the outputs obtained.

### What is this repository for? ###

* This repo contains the engine - sentiment_mod.py which basically gives you a positive or negative sentiment of a review or any text passed. For usage look at driver.py.
Also I have uploaded twitter_stream.py and plot.py which gives you live sentiment analysis on twiiter data pertaining to any topic. To use this download the source and in the file twitter_stream.py, fill out the consumer key and access token details, remove the line containing twitterapistuff and run this file and then plot.py to get a nice graph
* Language used - Python 2.7
* Training data - https://pythonprogramming.net/static/downloads/short_reviews/


### Who do I talk to? ###

* Repo owner or admin - Chetan Jaydeep(https://bitbucket.org/Chetan_WiredIn)