from api.get_available_ocr_resource_type import GetUAIOcrAvailResourceTypeApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class GetUAIOcrAvailOcrResourceTypeOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(GetUAIOcrAvailOcrResourceTypeOp, self).__init__(parser)

    def _add_args(self):
        super(GetUAIOcrAvailOcrResourceTypeOp, self)._add_args()

    def _parse_args(self, args):
        super(GetUAIOcrAvailOcrResourceTypeOp, self)._parse_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = GetUAIOcrAvailResourceTypeApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
        )
        return caller.call_api()
