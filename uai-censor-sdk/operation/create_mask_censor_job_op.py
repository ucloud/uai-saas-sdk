from api.create_mask_detection_job import UAICensorMaskJobApi

from operation.utils import parse_unrequired_args
from operation.base_datastream_operation import UAICensorBaseDatastreamOperation


class UAICensorCreateMaskJobOp(UAICensorBaseDatastreamOperation):
    def __init__(self, parser):
        super(UAICensorCreateMaskJobOp, self).__init__(parser)

    def _add_image_job_args(self, parser):
        args_parser = parser.add_argument_group(
            'Image-Params', 'Image Censor Job Parameters'
        )
        args_parser.add_argument(
            '--url',
            type=str,
            required=False,
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
        self.method = args['method']
        self.url = parse_unrequired_args(args, 'url')
        self.image = parse_unrequired_args(args, 'image')

    def _add_args(self):
        super(UAICensorCreateMaskJobOp, self)._add_args()
        self._add_image_job_args(self.parser)

    def _parse_args(self, args):
        super(UAICensorCreateMaskJobOp, self)._parse_args(args)
        self._parse_image_job_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = UAICensorCreateSyncImageJobApi(signature=self.signature,
                                                public_key=self.public_key,
                                                resource_id=self.resource_id,
                                                timestamp=self.timestamp,
                                                url=self.url,
                                                method=self.method,
                                                image=self.image)
        return caller.call_api()
