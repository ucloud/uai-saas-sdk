# -*- coding: utf-8 -*-  
from api.alg_tupu_api import UAITupuCensorApi
import time
public_key = ''
private_key = ''
resource_id = ''
if __name__ == '__main__':
    api_1 = UAITupuCensorApi(public_key, private_key, resource_id)
    with open('./test.jpg', 'rb') as fp:
            image = fp.read()
    succ, rsp = api_1.create_tupu_censor(
        method='file',
        productNames="tupu_porn,tupu_terror,tupu_politics",
        image = image
    )
    api_2 = UAITupuCensorApi(public_key, private_key, resource_id)
    succ, rsp = api_2.create_tupu_censor(
        method='url',
        url='http://5b0988e595225.cdn.sohucs.com/images/20171103/ac2da7fba0d447ff8565b81694b4da5d.jpeg',
        productNames="tupu_porn,tupu_terror,tupu_politics",
    )
