import sys
import time
from api.utils import load_config, gen_signature
from api.ocr_bill_job import UAIOcrBillJobApi

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = '../config_files/bill-config-online.json'

    url = 'http://uai-demo-adam.cn-bj.ufileos.com/bill.jpg'
    timestamp = int(time.time())
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, url=url)

    caller = UAIOcrBillJobApi(signature=signature, public_key=public_key, resource_id=resource_id,
                                             timestamp=timestamp, method='url',url=url)
    caller.call_api()