from api.get_available_censor_resource_type import GetUAICensorAvailResourceTypeApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAICensorBaseControllerOperation


class GetUAICensorAvailCensorResourceTypeOp(UAICensorBaseControllerOperation):

    def __init__(self, parser):
        super(GetUAICensorAvailCensorResourceTypeOp, self).__init__(parser)

    def _add_args(self):
        super(GetUAICensorAvailCensorResourceTypeOp, self)._add_args()

    def _parse_args(self, args):
        super(GetUAICensorAvailCensorResourceTypeOp, self)._parse_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = GetUAICensorAvailResourceTypeApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
        )
        return caller.call_api()
