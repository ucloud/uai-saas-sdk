from api.base_controller_api import UAIOcrBaseControllerApi


class CreateUAIOcrResourceApi(UAIOcrBaseControllerApi):

    ACTION_NAME = "CreateUAIOcrResource"

    def __init__(self, public_key, private_key, resource_types, region='', zone='', project_id='',  resource_name='', resource_memo=''):
        super(CreateUAIOcrResourceApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self._get_multi_params(resource_types, 'ResourceType')
        self.cmd_params['ResourceName'] = resource_name
        self.cmd_params['ResourceMemo'] = resource_memo

    def _check_args(self, params):
        if not self._check_multi_params(params, 'ResourceType'):
            return False
        return True

    def call_api(self):
        return super(CreateUAIOcrResourceApi, self).call_api()