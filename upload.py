#!/usr/bin/python3

import sys
from datetime import *
from pprint import *
import argparse

from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey
from videodata import VideoData


def getargs():
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    VideoData.add_args(parser)
    return parser.parse_args()


def video_build(args):
    video = VideoData()
    video.parse_args(args)
    return video


def video_upload(video):
    # Setup APIs
    api = GoogleAPIKey("test/client_secret.json")
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


if __name__ == '__main__':
    print("File run")
    video_upload(video_build(getargs()))

