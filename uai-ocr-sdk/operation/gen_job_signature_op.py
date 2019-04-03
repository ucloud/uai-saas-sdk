from api.gen_job_signature import UAIOcrGenJobSignatureApi

from operation.utils import parse_unrequired_args
from operation.base_controller_operation import UAIOcrBaseControllerOperation


class UAIOcrGenJobSignatureOp(UAIOcrBaseControllerOperation):

    def __init__(self, parser):
        super(UAIOcrGenJobSignatureOp, self).__init__(parser)
        self.params = {}

    def _add_signature_args(self, parser):
        args_parser = parser.add_argument_group(
            'Signature-Params', 'Signature Parameters'
        )
        args_parser.add_argument(
            '--config_file',
            type=str,
            required=True,
            help='config file path, should contain public key, private key and resource id'
        )
        args_parser.add_argument(
            '--url',
            type=str,
            required=False,
            help='url of current job, cannot be nil when gen signature for creating video jobs'
        )
        args_parser.add_argument(
            '--job_id',
            type=str,
            required=False,
            help='id of current job, cannot be nil when gen signature for querying video jobs'
        )

    def _parse_signature_args(self, args):
        self.config_file = args['config_file']
        self.url = parse_unrequired_args(args, 'url')
        self.job_id = parse_unrequired_args(args, 'job_id')


    def _add_args(self):
        self._add_signature_args(self.parser)

    def _parse_args(self, args):
        self._parse_signature_args(args)

    def cmd_run(self, args):
        self._parse_args(args)

        caller = UAIOcrGenJobSignatureApi(config_file=self.config_file,
                                             url=self.url,
                                             job_id=self.job_id)
        return caller.call_api()





