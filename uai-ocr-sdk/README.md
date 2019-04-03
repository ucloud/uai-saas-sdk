## UAI-OCR SDK工具说明文档

**Install**

```
sudo python setup.py install

```
####环境要求

- Python 2.7
- UAI-Ocr SDK
  - git clone https://github.com/ucloud/uai-saas-sdk.git
  - sudo python setup.py install


####UAI-OCR 工具一览

| 命令子类       | 命令名称       | 命令说明            |
| ---------- | ---------- | ------------------------ |
| resource   | create      | 创建资源 |
|            | delete      | 删除资源 |
|			 | modifyname  | 修改资源名称信息 |
| 			 | modifymemo  | 修改资源备注信息 |
|            | list        | 获取资源列表 |
|            | listtype    | 获取资源类型列表 |
|            | listrecord  | 获取资源请求记录 |
| signature  | gen         | 生成signature |
| ocr        | idcard      | 创建OCR任务 |


####使用说明

```
python ocr_tool.py resource {create,delete,modifyname,modifymemo,modifyoss,list,listrecord,listtype} ...
```

*注：[]表示可选*

####参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | String | 用户的公钥 |
| private_key | String | 用户的私钥 |
| project_id | String | bitmap的具体含义 |
| region | String | 地域信息，默认cn-bj2 |
| zone | String | 可用区信息，默认cn-bj2 |
| resource_types | String | 资源类型，若含多种资源，用","隔开|
| resource_name | String | 资源名称 |
| resource_memo | String | 资源备注 |
| limit  | String | 查询记录总数 |
| offset | String | 首条记录的偏移量 |

####1. 创建资源
  ```
  python ocr_tool.py resource create --public_key PUBLIC_KEY \
                                      	--private_key PRIVATE_KEY \
                                      	[--project_id PROJECT_ID] \
                                      	[--region REGION] \
                                      	[--zone ZONE] \
                                      	--resource_types RESOURCE_TYPES \
                                      	[--resource_name RESOURCE_NAME] \
                                      	[--resource_memo RESOURCE_MEMO]
  ```

####2. 删除资源

  ```
  python ocr_tool.py resource delete --public_key PUBLIC_KEY \
                                      	--private_key PRIVATE_KEY \
                                      	[--project_id PROJECT_ID] \
                                      	[--region REGION] \
                                      	[--zone ZONE] \
                                      	--resource_id RESOURCE_ID
  ```

####3. 修改资源名称

  ```
  python ocr_tool.py resource modifyname --public_key PUBLIC_KEY \
                                      	    --private_key PRIVATE_KEY \
                                      	    [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                      	    [--zone ZONE] \
                                      	    --resource_id RESOURCE_ID \
                                      	    --resource_name RESOURCE_NAME
 ```

####4. 修改资源备注

  ```
  python ocr_tool.py resource modifymemo --public_key PUBLIC_KEY \
                                      	    --private_key PRIVATE_KEY \
                                      	    [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                      	    [--zone ZONE] \
                                      	    --resource_id RESOURCE_ID \
                                      	    --resource_memo RESOURCE_MEMO
 ```


####5. 获取已创建资源列表

  ```
  python ocr_tool.py resource list --public_key PUBLIC_KEY \
                                      	    --private_key PRIVATE_KEY \
                                      	    [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                      	    [--zone ZONE] \
                                      	    [--limit LIMIT] \
                                      	    [--offset OFFSET]
 ```

####6. 获取可用资源类型

  ```
  python ocr_tool.py resource listtype --public_key PUBLIC_KEY \
                                      	    --private_key PRIVATE_KEY \
                                      	    [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                      	    [--zone ZONE] \
 ```

####7. 获取资源使用记录信息

```
  python ocr_tool.py resource listrecord   --public_key PUBLIC_KEY \
                                      	    --private_key PRIVATE_KEY \
                                      	    [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                      	    [--zone ZONE] \
                                      	    --begin_time BEGIN_TIME \
                                      	    --end_time END_TIME \
                                      	    [--resource_id RESOURCE_ID]
```


### 2. signature

▷ 使用说明

```
python ocr_tool.py signature {gen} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| config_file | String | 配置文件地址，包含基本账号信息以及资源ID |
| url | String | 文件地址 |
| job_id | Int | 任务ID |

- **gen: 生成签名信息**

  ```
  python ocr_tool.py signature gen	--config_file CONFIG_FILE \
  												[--url URL] \
  												[--job_id JOB_ID]
  ```


### 3. ocr

####使用说明

```
python ocr_tool.py ocr {idcard} ...
```

####参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | String | 用户的公钥 |
| resource_id | String | 资源ID|
| timestamp | Int | 时间戳信息|
| signature | String | 签名信息 |
| method | String | 身份证图片输入方法，可选项{url,file}|
| image | String | 图片内容 |
| url | String | 图片地址 |

####1. 创建OCR任务

  ```
  python ocr_tool.py image create  --signature SIGNATURE \
  										--public_key PUBLIC_KEY \
  										--resource_id RESOURCE_ID \
  										--timestamp TIMESTAMP \
  										--method {url, file} \
  										--scenes SCENES \
  										[--image IMAGE] \
  										[--url URL]
  ```



