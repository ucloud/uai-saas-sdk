import hashlib
import time
import json
from api.create_mask_detection_job import UAICensorMaskJobApi
def loadConfig(filename):
    ret = {}
    with open(filename, 'r') as fp:
        ret = json.loads(fp.read())
    return ret
def genSignature(prikey, params):
    items = list(params.items())
    items.sort()
    sign = ""
    for key, val in items:
        sign += str(key) + str(val)
    sign += prikey
    print (sign)
    hash_new = hashlib.sha1()
    hash_new.update(sign.encode(encoding='utf-8'))
    return hash_new.hexdigest()

timestamp = int(time.time())
url = 'http://uai-demo-adam.cn-bj.ufileos.com/adamtest_image.jpg'
conf = loadConfig('config.json')
public_key = conf['public_key']
private_key = conf['private_key']
resource_id = conf['resource_id']
params = {
    'Timestamp': timestamp,
    'Url': url,
    'PublicKey': public_key,
    'ResourceId': resource_id
}
signature = genSignature(private_key, params)
sdk = UAICensorMaskJobApi(signature, public_key, resource_id, timestamp, url, 'url')
print (sdk.call_api())
