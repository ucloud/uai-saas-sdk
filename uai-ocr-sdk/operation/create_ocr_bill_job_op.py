from api.ocr_bill_job import UAIOcrBillJobApi

from operation.utils import parse_unrequired_args
from operation.base_datastream_operation import UAIOcrBaseDatastreamOperation


class CreateUAIOcrBillJobOp(UAIOcrBaseDatastreamOperation):

    def __init__(self, parser):
        super(CreateUAIOcrBillJobOp, self).__init__(parser)

    def _add_bill_job_args(self, parser):
        args_parser = parser.add_argument_group(
            'IdCard-Params', 'IdCard Job Parameters'
        )
        args_parser.add_argument(
            '--url',
            type=str,
            required=False,
            help='Url of ocr image'
        )
        args_parser.add_argument(
            '--image',
            type=str,
            required=False,
            help='Content of ocr image'
        )
        args_parser.add_argument(
            '--method',
            type=str,
            choices=['url', 'file'],
            required=True,
            help='method of ocr image, choose from url, file'
        )

    def _parse_bill_job_args(self, args):
        self.url = parse_unrequired_args(args, 'url')
        self.image = parse_unrequired_args(args, 'image')
        self.method = args['method']

    def _add_args(self):
        super(CreateUAIOcrBillJobOp, self)._add_args()
        self._add_bill_job_args(self.parser)

    def _parse_args(self, args):
        super(CreateUAIOcrBillJobOp, self)._parse_args(args)
        self._parse_bill_job_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = UAIOcrBillJobApi(
            signature=self.signature,
            public_key=self.public_key,
            resource_id=self.resource_id,
            timestamp=self.timestamp,
            url=self.url,
            method=self.method,
            image=self.image
        )
        return caller.call_api()