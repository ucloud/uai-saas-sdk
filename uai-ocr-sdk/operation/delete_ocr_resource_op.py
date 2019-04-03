from api.delete_ocr_resource import DeleteUAIOcrResourceApi
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class DeleteOcrResourceOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(DeleteOcrResourceOp, self).__init__(parser)

    def _add_delete_resource_args(self, parser):
        args_parser = parser.add_argument_group(
            'Resource-Params', 'UAI Ocr Resource Parameters'
        )
        args_parser.add_argument(
            '--resource_id',
            type=str,
            required=True,
            help='Id of resource to be deleted'
        )

    def _parse_delete_resource_args(self, args):
        self.resource_id = args['resource_id']

    def _add_args(self):
        super(DeleteOcrResourceOp, self)._add_args()
        self._add_delete_resource_args(self.parser)

    def _parse_args(self, args):
        super(DeleteOcrResourceOp, self)._parse_args(args)
        self._parse_delete_resource_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = DeleteUAIOcrResourceApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_id=self.resource_id)
        return caller.call_api()