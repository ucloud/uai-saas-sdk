from api.modify_ocr_resource_memo import ModifyUAIOcrResourceMemoApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class ModifyUAIOcrResourceMemoOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(ModifyUAIOcrResourceMemoOp, self).__init__(parser)

    def _add_memo_args(self, parser):
        args_parser = parser.add_argument_group(
            'Memo-Params', 'UAI Ocr Resource Memo Params'
        )
        args_parser.add_argument(
            '--resource_id',
            type=str,
            required=True,
            help='Resource id to be modified'
        )
        args_parser.add_argument(
            '--resource_memo',
            type=str,
            required=True,
            help='resource memo after modified'
        )

    def _parse_memo_args(self, args):
        self.resource_id = args['resource_id']
        self.resource_memo = args['resource_memo']

    def _add_args(self):
        super(ModifyUAIOcrResourceMemoOp, self)._add_args()
        self._add_memo_args(self.parser)


    def _parse_args(self, args):
        super(ModifyUAIOcrResourceMemoOp, self)._parse_args(args)
        self._parse_memo_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = ModifyUAIOcrResourceMemoApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_id=self.resource_id,
            resource_memo=self.resource_memo
        )
        return caller.call_api()
