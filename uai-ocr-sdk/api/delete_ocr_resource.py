from api.base_controller_api import UAIOcrBaseControllerApi


class DeleteUAIOcrResourceApi(UAIOcrBaseControllerApi):

    ACTION_NAME = "DeleteUAIOcrResource"

    def __init__(self,  public_key, private_key, resource_id, region='', zone='', project_id=''):
        super(DeleteUAIOcrResourceApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['ResourceId'] = resource_id

    def _check_args(self, params):
        if params['ResourceId'] == '':
            return False
        return True

    def call_api(self):
        return super(DeleteUAIOcrResourceApi, self).call_api()