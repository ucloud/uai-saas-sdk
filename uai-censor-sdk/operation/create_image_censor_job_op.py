from api.create_sync_image_job import UAICensorCreateSyncImageJobApi

from operation.base_datastream_operation import UAICensorBaseDatastreamOperation


class UAICensorCreateImageJobOp(UAICensorBaseDatastreamOperation):
    def __init__(self, parser):
        super(UAICensorCreateImageJobOp, self).__init__(parser)

    def _add_image_job_args(self, parser):
        args_parser = parser.add_argument_group(
            'Image-Params', 'Image Censor Job Parameters'
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
            help='Url of censor image'
        )
        args_parser.add_argument(
            '--image',
            type=str,
            required=False,
            help='Content of censor image'
        )
        args_parser.add_argument(
            '--method',
            type=str,
            choices=['url', 'file'],
            required=True,
            help='method of censor image, choose from url, file'
        )

    def _parse_image_job_args(self, args):
        self.scenes = args['scenes']
        self.url = args['url']
        self.method = args['method']

    def _add_args(self):
        super(UAICensorCreateImageJobOp, self)._add_args()
        self._add_image_job_args(self.parser)

    def _parse_args(self, args):
        super(UAICensorCreateImageJobOp, self)._parse_args(args)
        self._parse_image_job_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = UAICensorCreateSyncImageJobApi(signature=self.signature,
                                                public_key=self.public_key,
                                                resource_id=self.resource_id,
                                                timestamp=self.timestamp,
                                                scenes=self.scenes,
                                                url=self.url,
                                                method=self.method)
        return caller.call_api()
