from api.utils import gen_sync_image_censor_url
from api.base_datastream_api import UAICensorBaseDatastreamApi


class UAICensorCreateSyncImageJobApi(UAICensorBaseDatastreamApi):

    REQUEST_URL = gen_sync_image_censor_url()

    def __init__(self, signature, public_key, resource_id, timestamp, scenes, url=None, method='url', image=None):
        super(UAICensorCreateSyncImageJobApi, self).__init__(self.REQUEST_URL,
                                                             signature, public_key,
                                                             resource_id, timestamp)
        self.cmd_params['Scenes'] = ','.join(scenes)
        self.cmd_params['Method'] = method.lower()
        if self.cmd_params['Method'] == 'url':
            self.cmd_params['Url'] = url
        else:
            self.cmd_params['Image'] = image

    def _check_args(self, header, params):
        if not super(UAICensorCreateSyncImageJobApi, self)._check_args(header, params):
            return False

        if params['Scenes'] == "":
            return False
        if params['Method'] not in ['url', 'file']:
            return False
        if params['Method'] == "url" and not params['Url']:
            return False
        if params['Method'] == 'file' and not params['Image']:
            return False
        if params['Method'] == "":
            return False
        return True

    def call_api(self):
        super(UAICensorCreateSyncImageJobApi, self).call_api()
        return super(UAICensorCreateSyncImageJobApi, self)._send_post_request_with_multi_part()
