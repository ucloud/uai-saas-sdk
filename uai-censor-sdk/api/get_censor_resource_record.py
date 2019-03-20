from api.base_controller_api import UAICensorBaseControllerApi


class GetUAICensorResourceRecordInfoApi(UAICensorBaseControllerApi):

    ACTION_NAME = "GetUAICensorResourceRecordInfo"

    def __init__(self, begin_time, end_time, public_key, private_key, region='', zone='', project_id='', resource_id='', limit=0, offset=0):
        super(GetUAICensorResourceRecordInfoApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['BeginTime'] = begin_time
        self.cmd_params['EndTime'] = end_time
        self.cmd_params['ResourceId'] = resource_id
        self.cmd_params['Limit'] = limit
        self.cmd_params['Offset'] = offset

    def _check_args(self, params):
        if params['BeginTime'] < 0 or params['BeginTime'] == 0 :
            raise ValueError("BeginTime should not be negative and should not be nil")
        if params['EndTime'] < 0 or params['EndTime'] == 0 :
            raise ValueError("EndTime should not be negative and should not be nil")
        if params['Limit'] < 0:
            raise ValueError("Limit should not be negative")
        if params['Offset'] < 0:
            raise ValueError("Offset should not be negative")
        return True

    def call_api(self):
        return super(GetUAICensorResourceRecordInfoApi, self).call_api()