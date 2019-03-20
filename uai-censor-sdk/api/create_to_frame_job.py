from api.utils import gen_async_video_toframe_url
from api.base_datastream_api import UAICensorBaseDatastreamApi

ToFrameMode_FirstView = 1
ToFrameMode_FullCut = 2


class UAICensorCreateAsyncToFrameJobApi(UAICensorBaseDatastreamApi):

    REQUEST_URL = gen_async_video_toframe_url()

    def __init__(self, signature, public_key, resource_id, timestamp, mode, url, bucket, prefix, interval=0, callback=''):
        super(UAICensorCreateAsyncToFrameJobApi, self).__init__(self.REQUEST_URL,
                                                                signature, public_key,
                                                                resource_id, timestamp)
        self.cmd_params['Mode'] = mode
        self.cmd_params['Url'] = url
        self.cmd_params['Interval'] = interval
        self.cmd_params['Bucket'] = bucket
        self.cmd_params['Prefix'] = prefix
        self.cmd_params['Callback'] = callback

    def _check_args(self, header, params):
        if not super(UAICensorCreateAsyncToFrameJobApi, self)._check_args(header, params):
            return False

        if params['Url'] == "":
            raise ValueError("Url cannot be nil in params")
        if params['Bucket'] == "":
            raise ValueError("Bucket cannot be nil in params")
        if params['Prefix'] == "":
            raise ValueError("Prefix cannot be nil in params")

        if params['Mode'] == 0:
            raise ValueError("Mode cannot be nil in params")
        if params['Mode'] != ToFrameMode_FirstView and params['Mode'] != ToFrameMode_FullCut:
           raise ValueError("Mode can only be chosen from {0}(FirstView) and {1}(FullCut)".
                            format(ToFrameMode_FirstView, ToFrameMode_FullCut))
        if params['Mode'] == ToFrameMode_FirstView:
            return True

        if params['Interval'] == 0:
            raise ValueError("Interval cannot be nil in params")
        return True

    def call_api(self):
        super(UAICensorCreateAsyncToFrameJobApi, self).call_api()
        return super(UAICensorCreateAsyncToFrameJobApi, self)._send_post_request()