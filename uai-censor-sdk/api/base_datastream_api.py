import json
import requests
from api.utils import get_response
from api.logger import uai_logger


class UAICensorBaseDatastreamApi(object):

    def __init__(self, cmd_url, signature, public_key, resource_id, timestamp):
        self.cmd_params = {}
        self.cmd_header = {}
        self.cmd_url = cmd_url
        self.cmd_header['Signature'] = signature
        self.cmd_header['PublicKey'] = public_key
        self.cmd_header['ResourceId'] = resource_id
        self.cmd_header['Timestamp'] = str(timestamp)

    def _check_args(self, header, params):
        if header['Signature'] == "":
            raise ValueError("Signature cannot be nil in header info")
        if header['PublicKey'] == "":
            raise ValueError("PublicKey cannot be nil in header info")
        if header['ResourceId'] == "":
            raise ValueError("ResourceId cannot be nil in header info")
        if header['Timestamp'] == "":
            raise ValueError("Timestamp cannot be nil in header info")
        return True

    def call_api(self):
        if not self._check_args(self.cmd_header, self.cmd_params):
            raise ValueError("Check API params error, header: {0}, params: {1}".
                             format(self.cmd_header, self.cmd_params))

    def _send_post_request(self):
        r = requests.post(self.cmd_url, data=json.dumps(self.cmd_params), headers=self.cmd_header)
        rsp = json.loads(r.text, encoding='utf-8')
        if rsp['RetCode'] != 0:
            print("Call {0} fail: [{1}]{2}".format(self.cmd_url, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            uai_logger.error("Call {0} fail: [{1}]{2}".format(self.cmd_url, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            return False, rsp
        else:
            print("Call {0} success: {1}".format(self.cmd_url, get_response(rsp, 0)))
            uai_logger.info("Call {0} success: {1}".format(self.cmd_url, get_response(rsp, 0)))
            return True, rsp

    def _send_post_request_with_multi_part(self):
        r = requests.post(self.cmd_url, files=self.cmd_params, headers=self.cmd_header)
        rsp = json.loads(r.text, encoding='utf-8')
        if rsp['RetCode'] != 0:
            print("Call {0} fail: [{1}]{2}".format(self.cmd_url, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            uai_logger.error("Call {0} fail: [{1}]{2}".format(self.cmd_url, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            return False, rsp
        else:
            print("Call {0} success: {1}".format(self.cmd_url, get_response(rsp, 0)))
            uai_logger.info("Call {0} success: {1}".format(self.cmd_url, get_response(rsp, 0)))
            return True, rsp

    def _send_get_request(self):
        r = requests.get(self.cmd_url, params=self.cmd_params, headers=self.cmd_header)
        rsp = json.loads(r.text, encoding='utf-8')
        if rsp['RetCode'] != 0:
            print("Call {0} fail: [{1}]{2}".format(self.cmd_url, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            uai_logger.error("Call {0} fail: [{1}]{2}".format(self.cmd_url, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            return False, rsp
        else:
            print("Call {0} success: {1}".format(self.cmd_url, get_response(rsp, 0)))
            uai_logger.info("Call {0} success: {1}".format(self.cmd_url, get_response(rsp, 0)))
            return True, rsp

