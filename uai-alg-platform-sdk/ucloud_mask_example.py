# -*- coding: utf-8 -*-  
from api.alg_ucloud_api import UAIUCloudApi
import time
public_key = ''
private_key = ''
resource_id = ''

if __name__ == '__main__':
    mask_api_1 = UAIUCloudApi(public_key, private_key, resource_id)
    with open('./test.jpg', 'rb') as fp:
            image = fp.read()
    succ, rsp = mask_api_1.create_ucloud_mask(
        method='file',
        image=image,
    )
    mask_api_2 = UAIUCloudApi(public_key, private_key, resource_id)
    succ, rsp = mask_api_2.create_ucloud_mask(
        method='url',
        url='http://test.png',
    )


    
