from api.base_datastream_api import UAICensorBaseDatastreamApi
from api.utils import gen_async_video_censor_url

class UAICensorCreateAsyncVideoJobApi(UAICensorBaseDatastreamApi):

    REQUEST_URL = gen_async_video_censor_url()

    def __init__(self, signature, public_key, resource_id, timestamp, scenes, url, interval, callback=''):
        super(UAICensorCreateAsyncVideoJobApi, self).__init__(self.REQUEST_URL,
                                                              signature, public_key,
                                                              resource_id, timestamp)
        self.cmd_params['Scenes'] = scenes
        self.cmd_params['Url'] = url
        self.cmd_params['Interval'] = interval
        self.cmd_params['Callback'] = callback

    def _check_args(self, header, params):
        if not super(UAICensorCreateAsyncVideoJobApi, self)._check_args(header, params):
            return False
        if len(params['Scenes']) == 0:
            return False
        if params['Url'] == "":
            return False
        if params['Interval'] == 0:
            return False
        return True

    def call_api(self):
        super(UAICensorCreateAsyncVideoJobApi, self).call_api()
        return super(UAICensorCreateAsyncVideoJobApi, self)._send_post_request()
