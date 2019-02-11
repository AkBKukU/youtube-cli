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
video.file_path = "./camerchange.mov"
video.categoryId = 28

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
#ytd.video_upload(video)

print(str(video))

