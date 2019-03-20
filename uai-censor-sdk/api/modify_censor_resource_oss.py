from api.base_controller_api import UAICensorBaseControllerApi


class ModifyUAICensorResourceOssInfoApi(UAICensorBaseControllerApi):

    ACTION_NAME = "ModifyUAICensorResourceOssInfo"

    def __init__(self, resource_id, oss_public_key, oss_private_key, public_key, private_key, region='', zone='', project_id=''):
        super(ModifyUAICensorResourceOssInfoApi, self).__init__(self.ACTION_NAME, public_key, private_key, region, zone, project_id)
        self.cmd_params['ResourceId'] = resource_id
        self.cmd_params['OssPublicKey'] = oss_public_key
        self.cmd_params['OssPrivateKey'] = oss_private_key

    def _check_args(self, params):
        if params['ResourceId'] == "":
            raise ValueError("ResourceId should not be nil")
        if params['OssPublicKey'] == "":
            raise ValueError("OssPublicKey should not be nil")
        if params['OssPrivateKey'] == "":
            raise ValueError("OssPrivateKey should not be nil")
        return True

    def call_api(self):
        return super(ModifyUAICensorResourceOssInfoApi, self).call_api()