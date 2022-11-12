# 必要なモジュールのimport
import pandas as pd
import tweepy
from pytz import timezone
import config

"""
メインの実行部分
ツイートデータの取得からデータの出力まで
"""

# APIキー
consumer_key = config.CK
consumer_secret = config.CS
access_token = config.AT
access_token_secret = config.ATS
bearer_token = config.BT

# tweepy.Clientでキーをセット
client = tweepy.Client(bearer_token, consumer_key,
                       consumer_secret, access_token, access_token_secret)

# ツイートデータの取得


# ツイートデータを番号順に出力


# ツイートデータをDataFrameにする


# DataFrameの出力


# ツイートデータのCSVへの出力


"""
ツイート情報を期間指定で収集
取得できるデータは直近1週間以内
RT+いいね数がrlcntを超えるツイートのみ取得
"""
# ツイートデータ取得部分 start_time, end_timeの期間で取得
response = client.search_recent_tweets(
    query="デイトラ",
    start_time="2022-01-23T00:00:00Z",
    end_time="2022-01-27T00:00:00Z",
    expansion=["author_id"],
    tweet_fields=["created_at", "public_metrics"],
    media_fields=["preview_image_url"],
    max_results=50
)
print(response)
