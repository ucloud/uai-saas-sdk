from api.base_controller_api import UAICensorBaseControllerApi


class CreateUAICensorResourceApi(UAICensorBaseControllerApi):

    ACTION_NAME = "CreateUAICensorResource"

    def __init__(self, public_key, private_key, resource_types, region='', zone='', project_id='',  resource_name='', resource_memo=''):
        super(CreateUAICensorResourceApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self._get_multi_params(resource_types, 'ResourceType')
        self.cmd_params['ResourceName'] = resource_name
        self.cmd_params['ResourceMemo'] = resource_memo

    def _check_args(self, params):
        if not self._check_multi_params(params, 'ResourceType'):
            return False
        return True

    def call_api(self):
        return super(CreateUAICensorResourceApi, self).call_api()