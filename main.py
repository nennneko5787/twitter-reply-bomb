import asyncio
import re
import random
import json
from datetime import datetime
from typing import List

import twikit

with open("settings.json") as f:
    settings = json.load(f)

with open("credentials.json") as f:
    credentials = json.load(f)

clients: List[twikit.Client] = []


def extractTweetInfo(url: str):
    match = re.search(r"https?://(?:www\.)?(twitter|x)\.com/([^/]+)/status/(\d+)", url)
    if match:
        address, username, tweet_id = match.groups()
        return username, tweet_id
    return None, None


async def main():
    print("Twitter-Reply-Bomb v2025.02.09")
    print("Created by nennneko5787 ( @Fng1Bot )")

    for i, c in enumerate(credentials, 1):
        if not c["enable"]:
            continue
        client = twikit.Client("ja-JP", proxy=settings["proxy"])
        await client.login(
            auth_info_1=c["username"],
            auth_info_2=c["email"],
            password=c["password"],
            cookies_file=f"./cookies/cookies_{i}.json",
            enable_ui_metrics=settings["enableUIMetrics"],
        )

        clientUser = await client.user()
        print(f"Logined as {clientUser.name} (@{clientUser.screen_name}) ({i})")
        clients.append(client)

    if not settings["urlPreset"]:
        url = input("URL of the tweet you want to send a reply cannon: ")
    else:
        url = settings["urlPreset"]
    _, tweetId = extractTweetInfo(url)
    tweets: List[twikit.Tweet] = []
    for client in clients:
        tweets.append(await client.get_tweet_by_id(tweetId))

    print(f"OK, fetched tweet ({tweets[0].id})")
    texts: List[str] = settings["textPresets"]
    if len(texts) <= 0:
        for i in range(1, settings["textsCount"]):
            texts.append(input(f"text({i}): "))

    print("Ready!")
    count = 0
    while True:
        if settings["replyCount"] > 0:
            if count >= settings["replyCount"]:
                break
        try:
            _one = datetime.now()
            text = f"{random.choice(texts)}{_one.strftime("(%Y/%m/%d %H:%M:%S)")}"
            tweet = random.choice(tweets)
            await tweet.reply(text)
            print(f"Tweeted: {text} ({datetime.now().timestamp() - _one.timestamp()})")
        except KeyboardInterrupt:
            break
        except Exception as e:
            raise e
        count += 1
        await asyncio.sleep(2.5)
    print("bye!")


asyncio.run(main())
