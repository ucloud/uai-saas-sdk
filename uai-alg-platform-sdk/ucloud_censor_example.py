# -*- coding: utf-8 -*-  
from api.alg_ucloud_api import UAIUCloudApi
import time
public_key = ''
private_key = ''
resource_id = ''

if __name__ == '__main__':
    api_1 = UAIUCloudApi(public_key, private_key, resource_id)
    with open('./test.jpg', 'rb') as fp:
            image = fp.read()
    succ, rsp = api_1.create_ucloud_censor(
        method='file',
        image=image,
        scenes = 'porn',
    )
    api_2 = UAIUCloudApi(public_key, private_key, resource_id)
    succ, rsp = api_2.create_ucloud_censor(
        method='url',
        url='http://test.png',
        scenes = 'porn',
    )


    
