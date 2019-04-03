from api.base_controller_api import UAIOcrBaseControllerApi


class GetUAIOcrAvailResourceTypeApi(UAIOcrBaseControllerApi):

    ACTION_NAME = "GetUAIOcrAvailResourceType"

    def __init__(self, public_key, private_key, region='', zone='', project_id=''):
        super(GetUAIOcrAvailResourceTypeApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)

    def _check_args(self, params):
        return True

    def call_api(self):
        return super(GetUAIOcrAvailResourceTypeApi, self).call_api()