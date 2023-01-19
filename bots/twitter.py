import time

import tweepy

from eli5.app import summarize
from secrets import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def start():
    all_tweets = []

    while True:
        tweets = api.mentions_timeline()

        if tweets == 0:
            return

        for tweet in tweets:
            try:
                if tweet not in all_tweets:
                    user = tweet.user.screen_name
                    tweet_text = tweet.text
                    summarized_text = summarize(tweet_text)
                    print(summarized_text)
                    tweet_to_post = f"@{user} - your ELI5: {summarized_text}"
                    print(tweet_to_post)

                    api.update_status(tweet_to_post)

                all_tweets.append(tweets)
            except Exception as err:
                print(f'Failed tweeting {tweet.text}')
                print(err)

        time.sleep(120)


if __name__ == '__main__':
    # Check we're authenticated
    try:
        api.verify_credentials()
        print("Authentication Successful")
    except Exception as e:
        print(e)

    start()
