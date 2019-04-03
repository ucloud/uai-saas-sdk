import time
from api.utils import load_config
from api.utils import gen_signature


class UAIOcrGenJobSignatureApi(object):

    def __init__(self, config_file, url=''):
       self.config_file = config_file
       self.url = url

    def _check_args(self):
        public_key, private_key, resource_id = load_config(self.config_file)
        if public_key == '':
            raise ValueError("Current config file: {0} invalid, public_key is empty".
                             format(self.config_file))
        if private_key == '':
            raise ValueError("Current config file: {0} invalid, private_key is empty".
                             format(self.config_file))
        if resource_id == '':
            raise ValueError("Current config file: {0} invalid, resource_id is empty".
                             format(self.config_file))

    def call_api(self):
        self._check_args()
        timestamp = int(time.time())
        signature = gen_signature(self.config_file, timestamp, self.url)
        print("Generated signature: {0}, timestamp: {1}\n".format(signature, timestamp))
        return signature, timestamp
