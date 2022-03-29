# name: Hylke Brouwer
# file: twitter_jou_jouw.py
# date: 23-03-2022
# code: Finds all tweets with 'jou' or 'jouw' in them and highlights them by color
#       (red for 'jou' and green for 'jouw'). Also counts the amount of occurences
#       for 'jou' and 'jou' individually, as well as all the tweets it ran through.
#       Given argument is compressed (.gz) file with json markup in which the actual 
#       content of the tweet is given with the key 'text'. (Used with karora, twitter 
#       corpus of RUG initially.)

import gzip
import json
import re
import sys


def main(argv):
    colored_r = '\033[91m'
    colored_g = '\033[92m'
    stop_color = '\033[0m'
    word_range = 3
    with gzip.open(argv[1], 'rt') as infile:
        total_tweets = 0
        total_jou = 0
        total_jouw = 0
        for single_tweet in infile:
            tweet = json.loads(single_tweet)
            tweet_text = tweet['text']
            if ' jou ' in tweet_text:
                p = re.compile(r'\w+')
                words_list = p.findall(tweet_text)
                index_jou = words_list.index('jou')
                total_tweets += 1
                total_jou += 1
                context_jou = words_list[(index_jou - word_range):(index_jou + word_range + 1)]
                for item in context_jou:
                    if item == 'jou':
                        print(colored_r + item + stop_color, end=' ')
                    else:
                        print(item, end=' ')
                print()
            elif ' jouw ' in tweet_text:
                p = re.compile(r'\w+')
                words_list = p.findall(tweet_text)
                index_jouw = words_list.index('jouw')
                total_tweets += 1
                total_jouw += 1
                context_jouw = words_list[(index_jouw - word_range):(index_jouw + word_range + 1)]
                for item in context_jouw:
                    if item == 'jouw':
                        print(colored_g + item + stop_color, end=' ')
                    else:
                        print(item, end=' ')
                print()
            else:
                total_tweets += 1
    
    print('\n===\n')
    print(f'Total amount of tweets tested were: {total_tweets}.')
    print(f'Total amount of tweets with jou in them: {colored_r + str(total_jou) + stop_color}.')
    print(f'Total amount of tweets with jouw in them: {colored_g + str(total_jouw) + stop_color}.')


if __name__ == '__main__':
    main(sys.argv)