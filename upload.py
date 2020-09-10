#!/usr/bin/python3

import sys
from datetime import *
from pprint import *
import argparse

from youtubecli.youtubeanalyticsapi import YTAnalytics
from youtubecli.youtubedataapi import YTData
from youtubecli.apikey import GoogleAPIKey
from youtubecli.videodata import VideoData


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
    api = GoogleAPIKey("client_secrets.json")
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
    #print(video_build(getargs()))
    video_upload(video_build(getargs()))

