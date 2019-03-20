from api.base_controller_api import UAICensorBaseControllerApi


class GetUAICensorAvailResourceTypeApi(UAICensorBaseControllerApi):

    ACTION_NAME = "GetUAICensorAvailResourceType"

    def __init__(self, public_key, private_key, region='', zone='', project_id=''):
        super(GetUAICensorAvailResourceTypeApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)

    def _check_args(self, params):
        return True

    def call_api(self):
        return super(GetUAICensorAvailResourceTypeApi, self).call_api()