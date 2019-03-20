from operation.utils import parse_unrequired_args
class UAICensorBaseControllerOperation(object):

    def __init__(self, parser):
        self.parser = parser
        self._add_args()

    def _add_account_args(self, parser):
        args_parser = parser.add_argument_group(
                         'User-Params', 'User Authentication Parameters')
        args_parser.add_argument(
            '--public_key',
            type=str,
            required=True,
            help='The public key of the user')
        args_parser.add_argument(
            '--private_key',
            type=str,
            required=True,
            help='The private key of the user')
        args_parser.add_argument(
            '--project_id',
            type=str,
            required=False,
            help='The project id of ucloud, could be null')
        args_parser.add_argument(
            '--region',
            type=str,
            required=False,
            help='The region to run the task, could be null')
        args_parser.add_argument(
            '--zone',
            type=str,
            required=False,
            help='The zone to run the task, could be null')

    def _parse_account_args(self, args):
        self.pub_key = args['public_key']
        self.pri_key = args['private_key']
        self.project_id = parse_unrequired_args(args, 'project_id')
        self.region = parse_unrequired_args(args, 'region')
        self.zone = parse_unrequired_args(args, 'zone')
        return True

    def _add_args(self):
       self._add_account_args(self.parser)

    def _parse_args(self, args):
       self._parse_account_args(args)

    def cmd_run(self, args):
        pass
