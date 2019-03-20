from api.base_controller_api import UAICensorBaseControllerApi


class DeleteUAICensorResourceApi(UAICensorBaseControllerApi):

    ACTION_NAME = "DeleteUAICensorResource"

    def __init__(self,  public_key, private_key, resource_id, region='', zone='', project_id=''):
        super(DeleteUAICensorResourceApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['ResourceId'] = resource_id

    def _check_args(self, params):
        if params['ResourceId'] == '':
            return False
        return True

    def call_api(self):
        return super(DeleteUAICensorResourceApi, self).call_api()