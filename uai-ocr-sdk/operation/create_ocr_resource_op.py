from api.create_ocr_resource import CreateUAIOcrResourceApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class CreateOcrResourceOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(CreateOcrResourceOp, self).__init__(parser)

    def _add_create_resource_args(self, parser):
        args_parser = parser.add_argument_group(
            'Resource-Params', 'UAI Ocr Resource Parameters'
        )
        args_parser.add_argument(
            '--resource_types',
            type=str,
            required=True,
            help='Type for current resource, '
                 'choose from "0(idcard)",'
                 'join with "," if with more than one scene'
        )

        args_parser.add_argument(
            '--resource_name',
            type=str,
            required=False,
            help='Name of current resource'
        )

        args_parser.add_argument(
            '--resource_memo',
            type=str,
            required=False,
            help='Memo of current resource'
        )

    def _parse_create_resource_args(self, args):
        self.resource_types = args['resource_types']
        self.resource_name = parse_unrequired_args(args, 'resource_name')
        self.resource_memo = parse_unrequired_args(args, 'resource_memo')

    def _add_args(self):
        super(CreateOcrResourceOp, self)._add_args()
        self._add_create_resource_args(self.parser)

    def _parse_args(self, args):
        super(CreateOcrResourceOp, self)._parse_args(args)
        self._parse_create_resource_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = CreateUAIOcrResourceApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_types=self.resource_types,
            resource_name=self.resource_name,
            resource_memo=self.resource_memo)
        return caller.call_api()
