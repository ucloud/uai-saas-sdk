class UAIOcrBaseDatastreamOperation(object):

    def __init__(self, parser):
        self.parser = parser
        self._add_args()

    def _add_header_args(self, parser):
        args_parser = parser.add_argument_group(
            'Header-Params', 'Request header Parameters'
        )
        args_parser.add_argument(
            '--signature',
            type=str,
            required=True,
            help='Signature gen by user'
        )
        args_parser.add_argument(
            '--public_key',
            type=str,
            required=True,
            help='Public key of current user'
        )
        args_parser.add_argument(
            '--resource_id',
            type=str,
            required=True,
            help='Resource id to be operated on'
        )
        args_parser.add_argument(
            '--timestamp',
            type=int,
            required=True,
            help='timestamp info'
        )

    def _add_args(self):
        self._add_header_args(self.parser)

    def _parse_header_args(self, args):
        self.signature = args['signature']
        self.public_key = args['public_key']
        self.resource_id = args['resource_id']
        self.timestamp = args['timestamp']

    def _parse_args(self, args):
        self._parse_header_args(args)

    def cmd_run(self, args):
        pass
