from api.delete_censor_resource import DeleteUAICensorResourceApi
from operation.base_controller_operation import UAICensorBaseControllerOperation


class DeleteCensorResourceOp(UAICensorBaseControllerOperation):

    def __init__(self, parser):
        super(DeleteCensorResourceOp, self).__init__(parser)

    def _add_delete_resource_args(self, parser):
        args_parser = parser.add_argument_group(
            'Resource-Params', 'UAI Censor Resource Parameters'
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
        super(DeleteCensorResourceOp, self)._add_args()
        self._add_delete_resource_args(self.parser)

    def _parse_args(self, args):
        super(DeleteCensorResourceOp, self)._parse_args(args)
        self._parse_delete_resource_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = DeleteUAICensorResourceApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            resource_id=self.resource_id)
        return caller.call_api()