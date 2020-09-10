#!/usr/bin/python3

import types
from pprint import pprint

from youtubecli.googleapi import GoogleAPIBase
from youtubecli.videodata import VideoData


class YTAnalytics(GoogleAPIBase):
    """Interface for the Youtube Analytics service

    Used for retrieving metrics info.
    """

    class Metrics:
        """Enum of metrics to request from the API"""
        estimatedRevenue = "estimatedRevenue", \
            VideoData.estimatedRevenue
        estimatedMinutesWatched = "estimatedMinutesWatched", \
            VideoData.estimatedMinutesWatched
        monetizedPlaybacks = "monetizedPlaybacks", \
            VideoData.monetizedPlaybacks
        views = "views", \
            VideoData.views

    def __init__(self):
        """Sets up API access information"""
        self.set_api("youtubeAnalytics","v1")
        self.add_scope("https://www.googleapis.com/auth/yt-analytics.readonly")
        self.add_scope("https://www.googleapis.com/auth/yt-analytics-monetary.readonly")
        self.m = self.Metrics()

    def set_channel_id(self, channel_id):
        """Set Youtube channel ID"""
        self.channel_id = channel_id

    def execute_query(self, start, end, metrics, video=None):
        """Execute a query with prepared metrics"""
        if video:
            filters = "video==" + video.id
        else:
            filters = ""

        return self.service.reports().query(
            ids="channel=="+self.channel_id,
            filters=filters,
            metrics=metrics,
            start_date=start.strftime("%Y-%m-%d"),
            end_date=end.strftime("%Y-%m-%d")
        ).execute()

    def get_metrics(self, start, end, metrics, video):
        """Get metrics for a video for a specific dates

        Datetime parameters are used to select a time range to search. Use
        metrics from the Metrics class in a list.
        """
        if end is None:
            end = start

        metricString = ""
        for m in metrics:
            metricString += m[0] + ","

        metricString = metricString[:-1]

        result = self.execute_query(start, end, metricString, video)

        for row in result.get("rows",  []):
            for i, value in enumerate(row):
                types.MethodType(metrics[i][1].fset, video)(value)

        return video

