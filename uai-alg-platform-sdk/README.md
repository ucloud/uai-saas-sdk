### UAI-Algothrim Python SDK

#### 1.SDK说明：

UAI-Algothrim服务API接入工具，提供包括安全审查、OCR等第三方算法服务在内的python接入工具。

#### 2.数据流接口说明：

- 目前提供的接口信息如下：

    | 接口名称 | 接口说明 | 接口归属 |
    |---|---|---|
    | create_ucloud_censor | UCloud内容审核 | UAI-Algorithm |
    | create_ucloud_mask | UCloud口罩检测 | UAI-Algorithm |
    | create_tupu_censor | 图普内容审核 | UAI-Algorithm |

- 参数说明

    | 参数名称 | 参数类型 | 参数说明 | 参数归属 |
    |---|---|---|---|
    | public_key | string | 用户公钥，用于生成访问数据流接口所需的signature | UAI-Algorithm |
    | private_key | string | 用户私钥，用于生成访问数据流接口所需的signature | UAI-Algorithm |
    | resource_id | string | 资源ID，通过控制流相关接口创建 | UAI-Algorithm |
    | scenes | string list | UCloud内容审核场景，目前支持的审核场景：'porn'| UAI-Algorithm |
    | method | string | 数据输入方式, 可选方法：'url', 'file'| UAI-Algorithm|
    | url | string | 数据路径 | UAI-Algorithm |
    | image | binary | 图片文件 | UAI-Algorithm |
    | productNames | string | 请求的产品（产品名称, 多个以逗号隔开）例如"tupu_porn,tupu_terror,tupu_politics"， | UAI-Algorithm |


- 使用样例

    - create_ucloud_censor UCloud内容审核
    
        ```
        api_1 = UAIUCloudApi(public_key, private_key, resource_id)
        with open('./test.png', 'rb') as fp:
            image = fp.read()
        succ, rsp = api_1.create_ucloud_censor(method='file',image=image,scenes = 'porn',)
        ```

    - create_ucloud_mask UCloud口罩检测

        ```
        mask_api_1 = UAIUCloudApi(public_key, private_key, resource_id)
        with open('./test.png', 'rb') as fp:
            image = fp.read()
        succ, rsp = mask_api_1.create_ucloud_mask(
            method='file',
            image=image,
        )
        ```

    - create_tupu_censor  图普内容审核

        ```
        api_1 = UAITupuCensorApi(public_key, private_key, resource_id)
        with open('./porn.jpg', 'rb') as fp:
            image = fp.read()
        succ, rsp = api_1.create_tupu_censor(
            method='file',
            productNames="tupu_porn,tupu_terror,tupu_politics",
            image = image
        )
        ```