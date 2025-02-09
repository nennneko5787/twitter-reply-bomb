import asyncio
import re
import random
import json
from datetime import datetime

import twikit

with open("credentials.json") as f:
    credentials = json.load(f)

clients: list[twikit.Client] = []


def extractTweetInfo(url: str):
    match = re.search(r"https?://(?:www\.)?(twitter|x)\.com/([^/]+)/status/(\d+)", url)
    if match:
        address, username, tweet_id = match.groups()
        return username, tweet_id
    return None, None


async def main():
    for i, c in enumerate(credentials, 1):
        if not c["enable"]:
            continue
        client = twikit.Client("ja-JP")
        await client.login(
            auth_info_1=c["username"],
            auth_info_2=c["email"],
            password=c["password"],
            cookies_file=f"cookies_{i}.json",
            enable_ui_metrics=True,
        )

        clientUser = await client.user()
        print(f"Logined as {clientUser.name} (@{clientUser.screen_name}) ({i})")
        clients.append(client)

    username, tweetId = extractTweetInfo(
        input("URL of the tweet you want to send a reply cannon: ")
    )
    tweets: list[twikit.Tweet] = []
    for client in clients:
        tweets.append(await client.get_tweet_by_id(tweetId))
    print("OK, fetched tweet")
    texts = []
    texts.append(input("text(1): "))
    texts.append(input("text(2): "))
    texts.append(input("text(3): "))
    texts.append(input("text(4): "))
    texts.append(input("text(5): "))
    while True:
        text = f"{random.choice(texts)}{datetime.now().strftime("(%Y/%m/%d %H:%M:%S)")}"
        await random.choice(tweets).reply(text)
        print(f"Tweeted: {text}")
        await asyncio.sleep(5)


asyncio.run(main())
