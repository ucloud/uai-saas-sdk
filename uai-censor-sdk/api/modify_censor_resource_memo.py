from api.base_controller_api import UAICensorBaseControllerApi


class ModifyUAICensorResourceMemoApi(UAICensorBaseControllerApi):

    ACTION_NAME = "ModifyUAICensorResourceMemo"

    def __init__(self, resource_id, resource_memo, public_key, private_key, region='', zone='', project_id=''):
        super(ModifyUAICensorResourceMemoApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['ResourceId'] = resource_id
        self.cmd_params['ResourceMemo'] = resource_memo

    def _check_args(self, params):
        if params['ResourceId'] == "":
            raise ValueError("ResourceId should not be nil")
        if params['ResourceMemo'] == "":
            raise ValueError("ResourceMemo should not be nil")
        return True

    def call_api(self):
        return super(ModifyUAICensorResourceMemoApi, self).call_api()