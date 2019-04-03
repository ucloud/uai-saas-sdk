from api.base_controller_api import UAIOcrBaseControllerApi


class ModifyUAIOcrResourceNameApi(UAIOcrBaseControllerApi):

    ACTION_NAME = "ModifyUAIOcrResourceName"

    def __init__(self, resource_id, resource_name, public_key, private_key, region='', zone='', project_id=''):
        super(ModifyUAIOcrResourceNameApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['ResourceId'] = resource_id
        self.cmd_params['ResourceName'] = resource_name

    def _check_args(self, params):
        if params['ResourceId'] == "":
            raise ValueError("ResourceId should not be nil")
        if params['ResourceName'] == "":
            raise ValueError("ResourceName should not be nil")
        return True

    def call_api(self):
        return super(ModifyUAIOcrResourceNameApi, self).call_api()