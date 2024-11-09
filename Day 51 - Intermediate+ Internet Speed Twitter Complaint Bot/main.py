from internet_speed_twitter_bot import InternetSpeedTwitterBot

if __name__ == "__main__":
    internet_speed_twitter_bot = InternetSpeedTwitterBot()
    internet_speed_twitter_bot.get_internet_speed()
    internet_speed_twitter_bot.tweet_at_provider()
