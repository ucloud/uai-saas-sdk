import json
import requests
from api.utils import verfy_ac
from api.utils import get_response
from api.logger import uai_logger


class UAICensorBaseControllerApi(object):

    UCLOUD_API_URL = 'http://api.ucloud.cn'
    PARAMS_DEFAULT_REGION = "cn-bj2"
    PARAMS_DEFAULT_ZONE = "cn-bj2-04"

    PARAM_ACTION = 'Action'
    PARAM_PUBLIC_KEY = 'PublicKey'
    PARAM_PROJECT_ID = 'ProjectId'
    PARAM_REGION = 'Region'
    PARAM_ZONE = 'Zone'

    def __init__(self, action, public_key, private_key, region='', zone='', project_id=''):
        self.cmd_params = {}

        self.action = action
        self.private_key = private_key
        self.cmd_url = self.UCLOUD_API_URL

        self.cmd_params[self.PARAM_ACTION] = action
        self.cmd_params[self.PARAM_PUBLIC_KEY] = public_key
        self.cmd_params[self.PARAM_REGION] = self.PARAMS_DEFAULT_REGION if region == '' else region
        self.cmd_params[self.PARAM_ZONE] = self.PARAMS_DEFAULT_ZONE if zone == '' else zone

        if project_id != '':
            self.cmd_params[self.PARAM_PROJECT_ID] = project_id

    def _check_args(self, params):
        pass

    def _cmd_common_request(self):
        if ('Signature' in self.cmd_params) is True:
            self.cmd_params.pop('Signature')
        self.cmd_params['Signature'] = verfy_ac(self.private_key,
                                                 self.cmd_params)
        uai_logger.info("Signature: {0}".format(self.cmd_params['Signature']))
        uai_logger.info(self.cmd_params)

        r = requests.get(self.cmd_url, params=self.cmd_params)
        rsp = json.loads(r.text, encoding="utf-8")
        if rsp["RetCode"] != 0:
            uai_logger.error("{0} fail: [{1}]{2}".format(self.action, rsp["RetCode"],
                                                              rsp["Message"].encode('utf-8')))
            return False, rsp
        else:
            del rsp['Action']
            print("{0} success: {1}".format(self.action, get_response(rsp, 0)))
            uai_logger.info("{0} success: {1}".format(self.action, get_response(rsp, 0)))
            return True, rsp

    def _get_multi_params(self, param_values, param_name):
        if param_values == '':
            self.cmd_params[param_name + '.' + '0'] = ''
            return
        params = param_values.split(',')
        i = 0
        for param in params:
            self.cmd_params[param_name + '.' + str(i)] = param
            i += 1
        return

    def _check_multi_params(self, params, param_name):
        if params[param_name + '.' + '0'] == '':
            return False
        i = 1
        while True:
            key_name = param_name + '.' + str(i)
            if key_name in params:
                if params[key_name] == '':
                    return False
                i += 1
            else:
                break
        return True

    def call_api(self):
        if not self._check_args(self.cmd_params):
            raise ValueError("Check API params error, params: {0}".format(self.cmd_params))
        return self._cmd_common_request()
