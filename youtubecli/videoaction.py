#!/usr/bin/python3

import sys
from datetime import *
from pprint import *
import argparse


from youtubecli.youtubeanalyticsapi import YTAnalytics
from youtubecli.youtubedataapi import YTData
from youtubecli.apikey import GoogleAPIKey
from youtubecli.videodata import VideoData

# Need to have a parent/super class that has arg adding and parsing functions
#   fort the action classes.
class VideoAction(object):

    def __init__(self,json_path=None):
        """Init with file path"""

    def add_args(parser):
        parser.add_argument('action',choices=["upload"], nargs='?', default='upload', help='Action to perform with video, defaults to upload')
        VideoData.add_args(parser)
        return parser

    def parse_args(args):
        video = VideoData()
        video.parse_args(args)

        if args.action == "upload":
            VideoAction.upload(video)

    def upload(video):
        # Setup APIs
        api = GoogleAPIKey()
        ytd = YTData()
        ytd.set_client(api)

        yta = YTAnalytics()
        yta.set_client(api)

        # Connect APIs
        ytd.connect()
        yta.connect()

        # upload
        ytd.video_upload(video)
        if video.thumbnail_path is not None:
            ytd.video_thumbnail_upload(video)

