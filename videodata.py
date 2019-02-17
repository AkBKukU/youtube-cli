#!/usr/bin/python
from jsonify import JSONify

class VideoData(JSONify):
    """Video data class for representing videos locally

    Video attributtes can be set or loaded from a JSON file. A video file and
    thumbnail path can also be specified if you are uploading or modifying a
    video.
    """

    percent_confidence_limit = 25

    # Privacy settings for uploaded video
    privacy_options = [
        ("public", "Everyone can see the video"),
        ("private", "Only you can see the video"),
        ("unlisted", "Anyone can see the video with the link"),
    ]

    category_options = [
        ( 2 ,"Cars & Vehicles"),
        ( 23 ,"Comedy"),
        ( 27 ,"Education"),
        ( 24 ,"Entertainment"),
        ( 1 ,"Film & Animation"),
        ( 20 ,"Gaming"),
        ( 26 ,"How-to & Style"),
        ( 10 ,"Music"),
        ( 25 ,"News & Politics"),
        ( 29 ,"Non-profits & Activism"),
        ( 22 ,"People & Blogs"),
        ( 15 ,"Pets & Animals"),
        ( 28 ,"Science & Technology"),
        ( 17 ,"Sport"),
        ( 19 ,"Travel & Events"),
    ]

    URL_edit_base = ("https://studio.youtube.com/video/","/edit")
    URL_watch_base = "https://www.youtube.com/?v="

    def add_args(parser):
        """Add options for creating a video object using parameters with argparse"""
        # attributtes
        parser.add_argument('--video-id', '-i', action="store", help='Video watch ID')
        parser.add_argument('--video-title', '-t', action="store", help='Video title')
        parser.add_argument('--video-description', '-d', action="store", help='Video description')
        parser.add_argument('--video-privacy', '-p', action="store", help='Video privacy status',choices=["private","unlisted","public"],default="unlisted")
        parser.add_argument('--video-category', '-c', action="store", help='Video category (by ID)',default=28,type=int)
        parser.add_argument('--video-tags', '-a', action="store", nargs='+', help='Video tags (space seperated list)')
        parser.add_argument('--video-file', '-f', action="store", help='Video file path')
        parser.add_argument('--video-thumbnail-file', '-u', action="store", help='Video thumbnail file path')

        # actions
        parser.add_argument('--video-json-file', '-l', action="store", help='Read JSON file for video data')
        return parser

    def parse_args(self,args):
        """Read options form parsearg to fill in video object attributtes"""
        #self.json_path = None
        if args.video_json_file is not None:
            self.json_path = args.video_json_file
            self.json_read()

        if args.video_file is not None:
            self.file_path = args.video_file
        if args.video_thumbnail_file is not None:
            self.thumbnail_path = args.video_thumbnail_file

        self.id = args.video_id
        self.title = args.video_title
        self.privacyStatus = args.video_privacy
        self.description = args.video_description
        self.categoryId = args.video_category
        self.tags = args.video_tags


    def __init__(self,json_path=None):
        """Initialize and load video info from JSON if provided"""
        super(VideoData, self).__init__(json_path)
        # Standard Data
        self._video_id = None
        self._title = None
        self._description = None
        self._published = None
        self._privacyStatus= None
        self._tags= None
        self._categoryId= None

        # Local Data
        self._file_path= None
        self._thumbnail_path= None

        # Virtual Feilds
        self._body= None
        self._URL_edit = None
        self._URL_watch = None

        # Metrics
        # TODO - Make a seperate analytics object to attach to video objects
        self._date_start = None
        self._date_end = None
        self._views = None
        self._monetizedPlaybacks = None
        self._estimatedRevenue = None
        self._estimatedMinutesWatched = None
        self._percent = None
        self._percent_confidence = None


    def __str__(self):
        """Basic info about video"""
        return  "Title: " + self._title +"\n"+\
                "Privacy: " + self._privacyStatus +"\n"+\
                "Watch: " + self.URL_watch +"\n"+\
                "Edit: " + self.URL_edit +"\n"+\
                "File: " + self._file_path

    @property
    def id(self):
        return self._video_id

    @id.setter
    def id(self, value):
        self._video_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._descrioption = value

    @property
    def published(self):
        return self._published

    @published.setter
    def published(self, value):
        self._published = value

    @property
    def privacyStatus(self):
        return self._privacyStatus

    @privacyStatus.setter
    def privacyStatus(self, value):
        found=False
        for status in self.privacy_options:
            if status[0] == value:
                found = True
                break

        if not found:
            raise ValueError('Invalid privacy status', value)
        self._privacyStatus= value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def categoryId(self):
        return self._categoryId

    @categoryId.setter
    def categoryId(self, value):
        found=False
        for cat in self.category_options:
            if cat[0] == value:
                found = True
                break

        if not found:
            raise ValueError('Invalid category ID', value)
        self._categoryId= value



    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        # File not found check will raise FileNotFoundError
        f = open(value)
        f.close()
        self._file_path = value

    @property
    def thumbnail_path(self):
        return self._thumbnail_path

    @thumbnail_path.setter
    def thumbnail_path(self, value):
        # File not found check will raise FileNotFoundError
        f = open(value)
        f.close()
        self._thumbnail_path = value

    @property
    def body(self):
        return dict(
            snippet=dict(
                title=self.title,
                description=self.description,
                tags=self.tags,
                categoryId=self.categoryId
            ),
            status=dict(
            privacyStatus=self.privacyStatus
            )
        )

    @body.setter
    def body(self, value):
        raise ValueError('Read only', value)


    @property
    def date_start(self):
        return self._date_start

    @date_start.setter
    def date_start(self, value):
        self._date_start = value

    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, value):
        self._date_end = value

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, value):
        self._views = value

    @property
    def monetizedPlaybacks(self):
        return self._monetizedPlaybacks

    @monetizedPlaybacks.setter
    def monetizedPlaybacks(self, value):
        self._monetizedPlaybacks = value

    @property
    def estimatedRevenue(self):
        return self._estimatedRevenue

    @estimatedRevenue.setter
    def estimatedRevenue(self, value):
        self._estimatedRevenue = value

    @property
    def estimatedMinutesWatched(self):
        return self._estimatedMinutesWatched

    @estimatedMinutesWatched.setter
    def estimatedMinutesWatched(self, value):
        self._estimatedMinutesWatched = value

    @property
    def percent(self):
        if self._percent is None and self.views > 0:
            self._percent = self._monetizedPlaybacks / self._views
            self._percent_confidence = self._views / \
                self.percent_confidence_limit
        else:
            self._percent = 0
            self._percent_confidence = 0
        return self._percent

    @percent.setter
    def percent(self, value):
        return self._percent

    @property
    def percent_confidence(self):
        return self._percent_confidence

    @property
    def URL_watch(self):
        return self.URL_watch_base + str(self.id)

    @property
    def URL_edit(self):
        return self.URL_edit_base[0] + str(self.id) + self.URL_edit_base[1]

