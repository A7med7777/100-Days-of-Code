import os

from dotenv import load_dotenv

from insta_follower import InstaFollower

load_dotenv()

URL = os.getenv("URL")
SIMILAR_ACOUNT_URL = os.getenv("SIMILAR_ACOUNT_URL")
FACEBOOK_PHONE = os.getenv("FACEBOOK_PHONE")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

if __name__ == "__main__":
    insta_follower = InstaFollower()
    insta_follower.login(FACEBOOK_PHONE or "", FACEBOOK_PASSWORD or "")
    insta_follower.find_followers(SIMILAR_ACOUNT_URL or "")
    insta_follower.follow()
    insta_follower.close()
