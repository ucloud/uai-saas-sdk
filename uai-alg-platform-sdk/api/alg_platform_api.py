import time
from api.utils import gen_signature
from api.base_datastream_api import UAIBaseDataStreamApi


class UAIAlgApi(UAIBaseDataStreamApi):

    param_method = 'Method'
    param_image = 'Image'

    method_value_url = 'url'
    method_value_file = 'file'


    callurl = 'http://api.uai.ucloud.cn'

    def __init__(self, public_key, private_key, resource_id):
        super(UAIAlgApi, self).__init__(public_key, private_key, resource_id)

    def _check_params(self):
        super(UAIAlgApi, self)._check_params()

    def _gen_signature(self, timestamp, url='', job_id=''):
        params = {
            self.param_timestamp: timestamp,
            self.param_public_key: self.public_key,
            self.param_resource_id: self.resource_id
        }
        if url != '':
            params[self.param_url] = url
        if job_id != '':
            params[self.param_job_id] = job_id
        return gen_signature(self.private_key, params)

    def create_tianrang_idcard(self, cgi, method, url='', image=None):
        self.api_url = '/'.join([self.callurl, cgi])
        method = method.lower()
        if method == self.method_value_url:
            if url == '':
                return False, '{0} cannot be empty'.format(self.param_url)
            self.cmd_params[self.param_url] = url
        elif method == self.method_value_file:
            if not image:
                return False, '{0} cannot be empty'.format(self.param_image)
            self.cmd_params[self.param_image] = image
        else:
            return False, '{0} should be chosen from {1},{2}, current is {3}'.format(self.param_method, self.method_value_url, self.method_value_file, method)

        self.cmd_params[self.param_method] = method

        timestamp = int(time.time())
        self.cmd_header[self.param_timestamp] = str(timestamp)
        self.cmd_header[self.param_signature] = self._gen_signature(timestamp=timestamp, url=url)

        print(self.cmd_header)

        try:
            self._check_params()
        except Exception as e:
            return False, 'check params fail: {0}'.format(e)
        return self.send_post_request_with_multi_part()
