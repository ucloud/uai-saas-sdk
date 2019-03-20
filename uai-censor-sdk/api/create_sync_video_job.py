from api.utils import gen_sync_video_censor_url
from api.base_datastream_api import UAICensorBaseDatastreamApi


class UAICensorCreateSyncVideoJobApi(UAICensorBaseDatastreamApi):

    REQUEST_URL = gen_sync_video_censor_url()

    def __init__(self, signature, public_key, resource_id, timestamp, scenes, url, interval):
        super(UAICensorCreateSyncVideoJobApi, self).__init__(self.REQUEST_URL,
                                                             signature, public_key,
                                                             resource_id, timestamp)
        self.cmd_params['Scenes'] = scenes
        self.cmd_params['Url'] = url
        self.cmd_params['Interval'] = interval

    def _check_args(self, header, params):
        if not super(UAICensorCreateSyncVideoJobApi, self)._check_args(header, params):
            return False

        if len(params['Scenes']) == 0:
            raise ValueError("Scenes cannot be nil in params")
        if params['Url'] == "":
            raise ValueError("Url cannot be nil in params")
        if params['Interval'] == 0:
            raise ValueError("Interval cannot be nil in params")
        return True

    def call_api(self):
        super(UAICensorCreateSyncVideoJobApi, self).call_api()
        return super(UAICensorCreateSyncVideoJobApi, self)._send_post_request()
