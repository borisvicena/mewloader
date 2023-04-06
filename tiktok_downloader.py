from TikTokApi import TikTokApi


api = TikTokApi()

for video in api.trending.videos():
    print(video.author.username)
