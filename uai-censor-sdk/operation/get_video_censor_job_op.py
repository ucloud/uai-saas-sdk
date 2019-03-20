from api.get_async_video_job import UAICensorGetAsyncVideoJobApi
from operation.base_datastream_operation import UAICensorBaseDatastreamOperation


class UAICensorGetVideoCensorJobOp(UAICensorBaseDatastreamOperation):
    def __init__(self, parser):
        super(UAICensorGetVideoCensorJobOp, self).__init__(parser)

    def _add_video_job_args(self, parser):
        args_parser = parser.add_argument_group(
            'Query-Params', 'Query Video Job Parameters'
        )
        args_parser.add_argument(
            '--job_id',
            type=str,
            required=True,
            help='Job id of video censor job'
        )

    def _parse_video_job_args(self, args):
        self.job_id = args['job_id']

    def _add_args(self):
        super(UAICensorGetVideoCensorJobOp, self)._add_args()
        self._add_video_job_args(self.parser)

    def _parse_args(self, args):
        super(UAICensorGetVideoCensorJobOp, self)._parse_args(args)
        self._parse_video_job_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = UAICensorGetAsyncVideoJobApi(signature=self.signature,
                                              public_key=self.public_key,
                                              resource_id=self.resource_id,
                                              timestamp=self.timestamp,
                                              job_id=self.job_id)
        return caller.call_api()
