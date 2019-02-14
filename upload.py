#!/usr/bin/python3

import sys
from datetime import *
from pprint import *

from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey
from videodata import VideoData

channel_id = ""

video = VideoData()
video.title = "test upload"
video.privacyStatus = "unlisted"
video.description = "test upload"
video.file_path = "./test/camerchange.mov"
video.thumbnail_path = "./test/thumbnail.png"
video.categoryId = 28
video.tags = ["test","tags","Does this work?"]

video.json_path = "video_save.json"
video.json_read()

print(str(video))

# Setup APIs
api = GoogleAPIKey("test/client_secret.json")
ytd = YTData()
ytd.set_client(api)
ytd.set_channel_id(channel_id)

yta = YTAnalytics()
yta.set_client(api)
yta.set_channel_id(channel_id)

# Connect APIs
ytd.connect()
yta.connect()


# upload
ytd.video_upload(video)
ytd.video_thumbnail_upload(video)


print(video)

pprint(vars(video))

