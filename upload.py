#!/usr/bin/python3

import sys
from datetime import *
from pprint import *

from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey
from videodata import VideoData

video = VideoData()
video.title = "test upload"
video.privacyStatus = "unlisted"
video.description = "test upload"
video.file_path = "./test/camerchange.mov"
video.thumbnail_path = "./test/thumbnail.png"
video.categoryId = 28
video.tags = ["test","tags","Does this work?"]

print(str(video))

m = YTAnalytics.Metrics()

# Setup APIs
api = GoogleAPIKey()
ytd = YTData()
ytd.set_client(api.get_client_id(), api.get_client_secret())
ytd.set_channel_id(api.channel_id)

yta = YTAnalytics()
yta.set_client(api.get_client_id(), api.get_client_secret())
yta.set_channel_id(api.channel_id)

# Connect APIs
ytd.connect()
yta.connect()


# Get all videos
video = ytd.video_upload_test(video)
ytd.video_thumbnail_upload(video)

print(video)

pprint(vars(video))

