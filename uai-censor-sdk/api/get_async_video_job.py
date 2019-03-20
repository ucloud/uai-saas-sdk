from api.base_datastream_api import UAICensorBaseDatastreamApi
from api.utils import gen_query_async_video_censor_url


class UAICensorGetAsyncVideoJobApi(UAICensorBaseDatastreamApi):

    REQUEST_URL = gen_query_async_video_censor_url()

    def __init__(self, signature, public_key, resource_id, timestamp, job_id):
        super(UAICensorGetAsyncVideoJobApi, self).__init__(self.REQUEST_URL,
                                                           signature, public_key,
                                                           resource_id, timestamp)
        self.cmd_params["JobId"] = job_id

    def _check_args(self, header, params):
        if not super(UAICensorGetAsyncVideoJobApi, self)._check_args(header, params):
            return False

        if params['JobId'] == "":
            return False
        return True

    def call_api(self):
        super(UAICensorGetAsyncVideoJobApi, self).call_api()
        return super(UAICensorGetAsyncVideoJobApi, self)._send_get_request()