#!/usr/bin/python3
from youtubecli.googleapi import GoogleAPIBase
from youtubecli.videodata import VideoData
from youtubecli.rupload import ReumableUpload

from datetime import *
import math
from pprint import *

from apiclient.http import MediaFileUpload

class YTData(GoogleAPIBase):
    """Interface for the Youtube Data service

    Used for retrieving basic video info and uploading videos.
    """


    channel_id = None

    def __init__(self):
        """Sets up API access information"""
        self.set_api("youtube", "v3")
        self.add_scope("https://www.googleapis.com/auth/youtube.force-ssl")
        self.add_scope("https://www.googleapis.com/auth/youtube.upload")
        self.add_scope("https://www.googleapis.com/auth/youtube.readonly")
        self.add_scope("https://www.googleapis.com/auth/youtubepartner")

    def set_channel_id(self, channel_id):
        """Set Youtube channel ID"""
        self.channel_id = channel_id

    def get_video_list(self, limit=0):
        """Get a list of all videos on the channel up to a limit"""
        max_loops = 50
        max_results = 50
        if limit:
            max_loops = math.floor(limit / 50)
            max_results = limit % 50

        end_of_videos = False
        videos = []
        timestamp = str(datetime.utcnow().replace(microsecond=0).isoformat()) \
            + "Z"

        # Get videos from API until the limit has been reached
        while not end_of_videos:
            result_limit = max_results if not max_loops else 50
            result = self.service.search().list(
                    part="snippet",
                    channelId=self.channel_id,
                    maxResults=result_limit,
                    order="date",
                    type='video',
                    publishedBefore = timestamp
                ).execute()

            for video in result.get("items", []):
                videos.append(VideoData())
                videos[-1].id = video.get("id").get("videoId")
                snippet = video.get("snippet", [])
                videos[-1].title = snippet.get("title")
                videos[-1].published = snippet.get("publishedAt")

            # Loop End
            max_loops = max_loops - 1
            if len(result.get("items", [])) < max_results or max_loops < 0:
                end_of_videos = True
            else:
                timestamp = videos[-1].published
                datestamp = datetime.strptime(
                        timestamp, "%Y-%m-%dT%H:%M:%S.%fZ"
                )
                datestamp = datestamp - timedelta(0, 1)
                timestamp = str(datestamp.replace(microsecond=0).isoformat()) \
                    + "Z"

        return videos

    def video_upload_test(self,video):
        """Upload test function because the quota usage is crazy high while testing"""
        print("Not Uploading: " + video.file_path)
        print(video)
        rupload = ReumableUpload()
        return rupload.upload_video_test(video)

    def video_upload(self,video):
        """Upload video to Youtube"""
        print("Uploading: " + video.file_path)
        insert_request = self.service.videos().insert(
            part=",".join(list(video.body.keys())),
            body=video.body,
            media_body=MediaFileUpload(
                video.file_path,
                chunksize=4*1024*1024,
                resumable=True
            )
        )
        rupload = ReumableUpload()
        return rupload.upload_video(video,insert_request)

    def video_thumbnail_upload(self,video):
        """Upload video thumbnail"""
        self.service.thumbnails().set(
            videoId=video.id,
            media_body=video.thumbnail_path
        ).execute()
        return


