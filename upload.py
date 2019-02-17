#!/usr/bin/python3

import sys
from datetime import *
from pprint import *
import argparse

from youtubeanalyticsapi import YTAnalytics
from youtubedataapi import YTData
from apikey import GoogleAPIKey
from videodata import VideoData

channel_id = ""

def getargs():
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('--channel-id', '-C', action="store", help='Youtube channel ID') # TODO - Create ChannelData class
    VideoData.add_args(parser)
    return parser.parse_args()


def video_build(args):
    channel_id = args.channel_id
    video = VideoData()
    video.parse_args(args)
    return video


def video_upload(video):
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


if __name__ == '__main__':
    print("File run")
    video_upload(video_build(getargs()))
