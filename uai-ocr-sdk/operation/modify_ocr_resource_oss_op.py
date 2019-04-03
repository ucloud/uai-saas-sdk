from api.modify_ocr_resource_oss import ModifyUAIOcrResourceOssInfoApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class ModifyUAIOcrResourceOssOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(ModifyUAIOcrResourceOssOp, self).__init__(parser)

    def _add_oss_args(self, parser):
        args_parser = parser.add_argument_group(
            'Oss-Params', 'UAI Ocr Modify Resource Oss Params'
        )
        args_parser.add_argument(
            '--resource_id',
            type=str,
            required=True,
            help='Resource id to be modified'
        )
        args_parser.add_argument(
            '--oss_public_key',
            type=str,
            required=True,
            help='oss public key after modified'
        )
        args_parser.add_argument(
            '--oss_private_key',
            type=str,
            required=True,
            help='oss private key after modified'
        )

    def _parse_oss_args(self, args):
        self.resource_id = args['resource_id']
        self.oss_public_key = args['oss_public_key']
        self.oss_private_key = args['oss_private_key']

    def _add_args(self):
        super(ModifyUAIOcrResourceOssOp, self)._add_args()
        self._add_oss_args(self.parser)

    def _parse_args(self, args):
        super(ModifyUAIOcrResourceOssOp, self)._parse_args(args)
        self._parse_oss_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = ModifyUAIOcrResourceOssInfoApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_id=self.resource_id,
            oss_public_key=self.oss_public_key,
            oss_private_key=self.oss_private_key
        )
        return caller.call_api()
