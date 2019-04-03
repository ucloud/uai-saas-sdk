from api.modify_ocr_resource_name import ModifyUAIOcrResourceNameApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class ModifyUAIOcrResourceNameOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(ModifyUAIOcrResourceNameOp, self).__init__(parser)

    def _add_name_args(self, parser):
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
            '--resource_name',
            type=str,
            required=True,
            help='resource name after modified'
        )

    def _parse_name_args(self, args):
        self.resource_id = args['resource_id']
        self.resource_name = args['resource_name']

    def _add_args(self):
        super(ModifyUAIOcrResourceNameOp, self)._add_args()
        self._add_name_args(self.parser)

    def _parse_args(self, args):
        super(ModifyUAIOcrResourceNameOp, self)._parse_args(args)
        self._parse_name_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = ModifyUAIOcrResourceNameApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_id=self.resource_id,
            resource_name=self.resource_name
        )
        return caller.call_api()
