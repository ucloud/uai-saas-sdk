from api.modify_censor_resource_memo import ModifyUAICensorResourceMemoApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAICensorBaseControllerOperation


class ModifyUAICensorResourceMemoOp(UAICensorBaseControllerOperation):

    def __init__(self, parser):
        super(ModifyUAICensorResourceMemoOp, self).__init__(parser)

    def _add_memo_args(self, parser):
        args_parser = parser.add_argument_group(
            'Memo-Params', 'UAI Censor Resource Memo Params'
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
        super(ModifyUAICensorResourceMemoOp, self)._add_args()
        self._add_memo_args(self.parser)


    def _parse_args(self, args):
        super(ModifyUAICensorResourceMemoOp, self)._parse_args(args)
        self._parse_memo_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = ModifyUAICensorResourceMemoApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_id=self.resource_id,
            resource_memo=self.resource_memo
        )
        return caller.call_api()
