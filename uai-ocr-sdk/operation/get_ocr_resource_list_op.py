from api.get_ocr_resource_list import GetUAIOcrResourceListApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class GetUAIOcrResourceListOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(GetUAIOcrResourceListOp, self).__init__(parser)

    def _add_list_resource_args(self, parser):
        args_parser = parser.add_argument_group(
            'List-Params', 'UAI Ocr Resource List Params'
        )
        args_parser.add_argument(
            '--limit',
            type=int,
            default=0,
            help='limit length of list items'
        )
        args_parser.add_argument(
            '--offset',
            type=int,
            default=0,
            help='offset of list items'
        )

    def _parse_list_resource_args(self, args):
        self.limit = args['limit']
        self.offset = args['offset']

    def _add_args(self):
        super(GetUAIOcrResourceListOp, self)._add_args()
        self._add_list_resource_args(self.parser)

    def _parse_args(self, args):
        super(GetUAIOcrResourceListOp, self)._parse_args(args)
        self._parse_list_resource_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = GetUAIOcrResourceListApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            limit=self.limit,
            offset=self.offset
        )
        return caller.call_api()
