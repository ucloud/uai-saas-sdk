from api.get_censor_resource_record import GetUAICensorResourceRecordInfoApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAICensorBaseControllerOperation


class GetUAICensorResourceRecordInfoOp(UAICensorBaseControllerOperation):

    def __init__(self, parser):
        super(GetUAICensorResourceRecordInfoOp, self).__init__(parser)

    def _add_list_record_args(self, parser):
        args_parser = parser.add_argument_group(
            'List-Params', 'UAI Censor Resource List Params'
        )
        args_parser.add_argument(
            '--begin_time',
            type=int,
            required=True,
            help='begin query time'
        )
        args_parser.add_argument(
            '--end_time',
            type=int,
            required=True,
            help='end query time'
        )
        args_parser.add_argument(
            '--resource_id',
            type=str,
            required=False,
            help='resource id, if not given, get record infos of all resources'
        )

    def _parse_list_record_args(self, args):
        self.begin_time = args['begin_time']
        self.end_time = args['end_time']
        self.resource_id = parse_unrequired_args(args, 'resource_id')

    def _add_args(self):
        super(GetUAICensorResourceRecordInfoOp, self)._add_args()
        self._add_list_record_args(self.parser)


    def _parse_args(self, args):
        super(GetUAICensorResourceRecordInfoOp, self)._parse_args(args)
        self._parse_list_record_args(args)

    def cmd_run(self, args):
        self._parse_args(args)
        caller = GetUAICensorResourceRecordInfoApi(
            public_key=self.pub_key,
            private_key=self.pri_key,
            region=self.region,
            zone=self.zone,
            project_id=self.project_id,
            begin_time=self.begin_time,
            end_time=self.end_time,
            resource_id=self.resource_id,
        )
        return caller.call_api()
