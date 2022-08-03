#!/usr/bin/python3
from youtubecli.jsonify import JSONify

class GoogleAPIKey(JSONify):
    """Wrapper interface for handling API key

    Get an API key from: https://support.google.com/googleapi/answer/6158862

    You can download a JSON file with your client_id and client_secret to load
    with this class.
    """
    
    json_path = "./client_secrets.json"

    def __init__(self,json_path=None):
        """Initialize and load key from JSON if provided"""
    
        self._client_id = None
        self._client_secret = None

    def add_args(parser):
        """Add options for API access using parameters with argparse"""
        parser.add_argument('--client', '-s', action="store", help='client_secrets JSON location')
        
        return parser


    def parse_args(args):
        """Read options form parsearg to fill in API object attributtes"""
        
        if args.client is not None:
            GoogleAPIKey.json_path = args.client
            
    def read_client(self):
        self.json_read(GoogleAPIKey.json_path)
        if hasattr(self, 'installed'):
            self._client_id = self.installed["client_id"]
            self._client_secret = self.installed["client_secret"]
        else:
            self._client_id = ""
            self._client_secret = ""
        

    @property
    def client_id(self):
        if self._client_id is None:
            self.read_client()
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def client_secret(self):
        if self._client_secret is None:
            self.read_client()
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        self._client_secret = value

