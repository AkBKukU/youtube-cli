#!/usr/bin/python3

import sys
from datetime import *
from pprint import *
import argparse

from youtubecli.youtubeanalyticsapi import YTAnalytics
from youtubecli.youtubedataapi import YTData
from youtubecli.apikey import GoogleAPIKey
from youtubecli.videodata import VideoData
from youtubecli.videoaction import VideoAction


def getargs():
    parser = argparse.ArgumentParser(conflict_handler='resolve')

    # Add main action modes
    parser.add_argument('mode',choices=["video"], nargs='?', default='video', help='Set mode to work in, defaults to video')
    # Override help to allow for a dynamic help screen.
    parser.add_argument('--help','-h', action='store_true',  help='Print this help screen')
    # Determine mode and get args for it
    args_mode,other=parser.parse_known_args()
    if args_mode.mode=="video":
        VideoAction.add_args(parser)

    # If help run print that and exit with all args
    if args_mode.help:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def parse_args(args):

    if args.mode=="video":
        VideoAction.parse_args(args)


if __name__ == '__main__':
    parse_args(getargs())
    #video_upload(video_build(getargs()))

