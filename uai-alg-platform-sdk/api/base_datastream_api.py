import json
import requests
from api.uai_logger import uai_logger
from api.utils import format_response


class UAIBaseDataStreamApi(object):

    param_signature = 'Signature'
    param_public_key = 'PublicKey'
    param_resource_id = 'ResourceId'
    param_timestamp = 'Timestamp'
    param_url = 'Url'
    param_job_id = 'JobId'

    def __init__(self, public_key, private_key, resource_id):

        self.cmd_params = {}
        self.cmd_header = {}

        self.api_url = ''

        self.public_key = public_key
        self.private_key = private_key
        self.resource_id = resource_id
        self.cmd_header[self.param_public_key] = public_key
        self.cmd_header[self.param_resource_id] = resource_id

    def _check_params(self):
        if self.cmd_header[self.param_public_key] == '':
            raise ValueError('{0} cannot be empty'.format(self.param_public_key))
        if self.cmd_header[self.param_resource_id] == '':
            raise ValueError('{0} cannot be empty'.format(self.param_resource_id))
        if self.cmd_header[self.param_timestamp] == '':
            raise ValueError('{0} cannot be empty'.format(self.param_timestamp))
        if self.cmd_header[self.param_signature] == '':
            raise ValueError('{0} cannot be empty'.format(self.param_signature))

    def send_post_request(self):
        r = requests.post(self.api_url, data=json.dumps(self.cmd_params), headers=self.cmd_header)
        rsp = json.loads(r.text, encoding='utf-8')
        if rsp['RetCode'] != 0:
            err_message = "call {0} fail, retCode: {1}, message: {2}".format(self.api_url, rsp["RetCode"], rsp["Message"].encode('utf-8'))
            uai_logger.error(err_message)
            print(err_message)
            return False, rsp
        else:
            response_message = 'call {0} success, response: {1}'.format(self.api_url, format_response(rsp, 0))
            uai_logger.info(response_message)
            print(response_message)
            return True, rsp

    def send_post_request_with_multi_part(self):
        r = requests.post(self.api_url, files=self.cmd_params, headers=self.cmd_header)
        rsp = json.loads(r.text, encoding='utf-8')
        if rsp['RetCode'] != 0:
            err_message = "call {0} fail, retCode: {1}, message: {2}".format(self.api_url, rsp["RetCode"], rsp["Message"].encode('utf-8'))
            uai_logger.error(err_message)
            print(err_message)
            return False, rsp
        else:
            response_message = 'call {0} success, response: {1}'.format(self.api_url, format_response(rsp, 0))
            uai_logger.info(response_message)
            print(response_message)
            return True, rsp

    def send_get_request(self):
        r = requests.get(self.api_url, params=self.cmd_params, headers=self.cmd_header)
        rsp = json.loads(r.text, encoding='utf-8')
        if rsp['RetCode'] != 0:
            err_message = "call {0} fail, retCode: {1}, message: {2}".format(self.api_url, rsp["RetCode"], rsp["Message"].encode('utf-8'))
            uai_logger.error(err_message)
            print(err_message)
            return False, rsp
        else:
            response_message = 'call {0} success, response: {1}'.format(self.api_url, format_response(rsp, 0))
            uai_logger.info(response_message)
            print(response_message)
            return True, rsp
