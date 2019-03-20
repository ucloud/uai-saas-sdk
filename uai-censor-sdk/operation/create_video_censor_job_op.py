import string

from api.create_sync_video_job import UAICensorCreateSyncVideoJobApi
from api.create_async_video_job import UAICensorCreateAsyncVideoJobApi

from operation.utils import parse_unrequired_args
from operation.base_datastream_operation import UAICensorBaseDatastreamOperation


class UAICensorCreateVideoJobOp(UAICensorBaseDatastreamOperation):
    def __init__(self, parser):
        super(UAICensorCreateVideoJobOp, self).__init__(parser)

    def _add_video_job_args(self, parser):
        args_parser = parser.add_argument_group(
            'Video-Params', 'Video Censor Job Parameters'
        )
        args_parser.add_argument(
            '--type',
            type=str,
            required=True,
            choices=['sync', 'async'],
            help='Censor type for current job, '
                 'choose from "sync, async"'
        )
        args_parser.add_argument(
            '--scenes',
            type=str,
            required=True,
            help='Scenes for current job, '
                 'choose from "porn, politician, terror",'
                 'join with "," if with more than one scene'
        )
        args_parser.add_argument(
            '--url',
            type=str,
            required=True,
            help='Url of censor video'
        )

        args_parser.add_argument(
            '--interval',
            type=int,
            required=False,
            default=25,
            help='Frame interval for current video, default is 25'
        )

        args_parser.add_argument(
            '--callback',
            type=str,
            required=False,
            help='User callback url'
        )

    def _parse_video_job_args(self, args):
        self.censor_type = args['type']
        scenes = args['scenes']
        self.scenes = string.split(scenes, ",")
        self.url = args['url']
        self.interval = args['interval']
        self.callback = parse_unrequired_args(args, 'callback')

    def _add_args(self):
        super(UAICensorCreateVideoJobOp, self)._add_args()
        self._add_video_job_args(self.parser)

    def _parse_args(self, args):
        super(UAICensorCreateVideoJobOp, self)._parse_args(args)
        self._parse_video_job_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        if self.censor_type == "sync":
            caller = UAICensorCreateSyncVideoJobApi(signature=self.signature,
                                                    public_key=self.public_key,
                                                    resource_id=self.resource_id,
                                                    timestamp=self.timestamp,
                                                    scenes=self.scenes,
                                                    url=self.url,
                                                    interval=self.interval)
        else:
            caller = UAICensorCreateAsyncVideoJobApi(signature=self.signature,
                                                     public_key=self.public_key,
                                                     resource_id=self.resource_id,
                                                     timestamp=self.timestamp,
                                                     scenes=self.scenes,
                                                     url=self.url,
                                                     interval=self.interval,
                                                     callback=self.callback)

        return caller.call_api()
