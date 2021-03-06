from api.base_controller_api import UAICensorBaseControllerApi


class GetUAICensorResourceListApi(UAICensorBaseControllerApi):

    ACTION_NAME = "GetUAICensorResourceList"

    def __init__(self, public_key, private_key, region='', zone='', project_id='', limit=0, offset=0, ):
        super(GetUAICensorResourceListApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['Limit'] = limit
        self.cmd_params['Offset'] = offset

    def _check_args(self, params):
        if params['Limit'] < 0:
            raise ValueError("Limit should not be negative")
        if params['Offset'] < 0:
            raise ValueError("Offset should not be negative")
        return True

    def call_api(self):
        return super(GetUAICensorResourceListApi, self).call_api()