from api.get_censor_resource_list import GetUAICensorResourceListApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAICensorBaseControllerOperation


class GetUAICensorResourceListOp(UAICensorBaseControllerOperation):

    def __init__(self, parser):
        super(GetUAICensorResourceListOp, self).__init__(parser)

    def _add_list_resource_args(self, parser):
        args_parser = parser.add_argument_group(
            'List-Params', 'UAI Censor Resource List Params'
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
        super(GetUAICensorResourceListOp, self)._add_args()
        self._add_list_resource_args(self.parser)

    def _parse_args(self, args):
        super(GetUAICensorResourceListOp, self)._parse_args(args)
        self._parse_list_resource_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = GetUAICensorResourceListApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            limit=self.limit,
            offset=self.offset
        )
        return caller.call_api()
