
from operation.utils import parse_unrequired_args
from api.create_to_frame_job import UAICensorCreateAsyncToFrameJobApi
from api.create_to_frame_job import ToFrameMode_FirstView
from operation.base_datastream_operation import UAICensorBaseDatastreamOperation


class UAICensorCreateVideoToFrameFirstViewJobOp(UAICensorBaseDatastreamOperation):
    def __init__(self, parser):
        super(UAICensorCreateVideoToFrameFirstViewJobOp, self).__init__(parser)

    def _add_video_job_args(self, parser):
        args_parser = parser.add_argument_group(
            'Video-Params', 'Video Censor Job Parameters'
        )
        args_parser.add_argument(
            '--url',
            type=str,
            required=True,
            help='Url of censor video'
        )
        args_parser.add_argument(
            '--bucket',
            type=str,
            required=True,
            help='Ufile bucket name'
        )

        args_parser.add_argument(
            '--prefix',
            type=str,
            required=True,
            help='Frame save prefix'
        )

    def _parse_video_job_args(self, args):
        self.url = args['url']
        self.bucket = args['bucket']
        self.prefix = args['prefix']

    def _add_args(self):
        super(UAICensorCreateVideoToFrameFirstViewJobOp, self)._add_args()
        self._add_video_job_args(self.parser)

    def _parse_args(self, args):
        super(UAICensorCreateVideoToFrameFirstViewJobOp, self)._parse_args(args)
        self._parse_video_job_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = UAICensorCreateAsyncToFrameJobApi(signature=self.signature,
                                                   public_key=self.public_key,
                                                   resource_id=self.resource_id,
                                                   timestamp=self.timestamp,
                                                   mode=ToFrameMode_FirstView,
                                                   url=self.url,
                                                   bucket=self.bucket,
                                                   prefix=self.prefix)
        return caller.call_api()
