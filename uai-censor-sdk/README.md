### UAI-Censor SDK工具说明文档

*Install*

```
sudo python setup.py install

```

► UAI-Censor 工具一览

| 命令子类       | 命令名称       | 命令说明            |
| ---------- | ---------- | ------------------------ |
| resource   | create      | 创建UAI审查资源 |
|            | delete      | 删除UAI审查资源 |
|			   | modifyname  | 修改资源名称信息 |
| 			   | modifymemo  | 修改资源备注信息 |
|            | modifyoss   | 修改资源oss授权信息 |
|            | list        | 获取资源列表 |
|            | listtype    | 获取资源类型列表 |
|            | listrecord  | 获取资源请求记录 |
| video      | create      | 创建UAI视频审查任务 |
|            | query       | 查询UAI视频审查任务状态 |
| image      | create      | 创建UAI图片审查任务 |
|            | query       | 查询UAI图片审查任务状态|
| frame      | fullcut     | 创建UAI截帧任务, 获取完整视频的截图 |
|			   | snapshot    | 创建UAI截帧任务, 获取视频的首张图片 |
|            | query       | 查询UAI截帧任务状态 |
| signature  | gen         | 生成signature |

► 使用说明

```
cd tools/censor_tool.py

python censor_tool.py {resource,video,image,frame,signature} ...
```
### 1. resource

▷ 使用说明

```
python censor_tool.py resource {create,delete,modifyname,modifymemo,modifyoss,list,listrecord,listtype} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | string | 用户的公钥 |
| private_key | string | 用户的私钥 |
| project_id | string | bitmap的具体含义 |
| region | string | 地域信息，默认cn-bj2 |
| zone | string | 可用区信息，默认cn-bj2 |
| resource_types | string | 资源类型，若含多种资源，用","隔开|
| resource_name | string | 资源名称 |
| resource_memo | string | 资源备注 |
| limit  | string | 查询记录总数 |
| offset | string | 首条记录的偏移量 |

- **create: 创建UAI安全审查资源**
  ```
  python censor_tool.py resource create --public_key PUBLIC_KEY \
                                      	--private_key PRIVATE_KEY \
                                      	[--project_id PROJECT_ID] \
                                      	[--region REGION] \
                                      	[--zone ZONE] \
                                      	--resource_types RESOURCE_TYPES \
                                      	[--resource_name RESOURCE_NAME] \
                                      	[--resource_memo RESOURCE_MEMO]
  ```

- **delete: 删除UAI安全审查资源**

  ```
  python censor_tool.py resource delete --public_key PUBLIC_KEY \
                                      	--private_key PRIVATE_KEY \
                                      	[--project_id PROJECT_ID] \
                                      	[--region REGION] \
                                      	[--zone ZONE] \
                                      	--resource_id RESOURCE_ID
  ```

- **modifyname: 修改UAI安全审查资源名称**

  ```
  python censor_tool.py resource modifyname --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --resource_id RESOURCE_ID \
                                            --resource_name RESOURCE_NAME
  ```

- **modifymemo: 修改UAI安全审查资源备注**

  ```
  python censor_tool.py resource modifymemo --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --resource_id RESOURCE_ID \
                                            --resource_memo RESOURCE_MEMO
  ```

- **modifyoss: 修改UAI安全审查oss授权信息**

  ```
  python censor_tool.py resource modifyoss  --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --resource_id RESOURCE_ID \
                                            --oss_public_key OSS_PUBLIC_KEY \
                                            --oss_private_key OSS_PRIVATE_KEY

  ```

- **list: 获取UAI安全审查资源列表**

  ```
  python censor_tool.py resource list   --public_key PUBLIC_KEY \
                                        --private_key PRIVATE_KEY \
                                        [--project_id PROJECT_ID] \
                                        [--region REGION] \
                                        [--zone ZONE] \
                                        [--limit LIMIT] \
                                        [--offset OFFSET]
  ```

- **listtype: 获取UAI安全审查可用资源类型**

  ```
  python censor_tool.py resource listtype   --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE]
  ```

- **listrecord: 获取UAI安全审查资源使用记录信息**

  ```
  python censor_tool.py resource listrecord --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --begin_time BEGIN_TIME \
                                            --end_time END_TIME \
                                            [--resource_id RESOURCE_ID]
  ```

### 2. video

▷ 使用说明

```
python censor_tool.py video {create,query} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | string | 用户的公钥 |
| resource_id | string | 资源ID|
| timestamp | int64 | 时间戳信息|
| url | string | 视频路径 |
| signature | string | 签名信息 |
| type | string | 视频审查任务类型，可选项{sync,async}|
| scenes | string | 视频审查场景，若有多个，用","分隔，可选项{porn, politician, terror}|
| interval | int | 截帧间隔 |
| callback | string | 视频审查结果回调地址 |

- **create: 创建UAI视频审查任务**

  ```
  python censor_tool.py video create    --signature SIGNATURE \
                                        --public_key PUBLIC_KEY \
                                        --resource_id RESOURCE_ID \
                                        --timestamp TIMESTAMP
                                        --type {sync,async} \
                                        --scenes SCENES \
                                        --url URL \
                                        [--interval INTERVAL] \
                                        [--callback CALLBACK]
  ```

- **query: 查看UAI视频审查任务**

  ```
  python censor_tool.py video query --signature SIGNATURE \
                                    --public_key PUBLIC_KEY \
                                    --resource_id RESOURCE_ID \
                                    --timestamp TIMESTAMP \
                                    --job_id JOB_ID
  ```

### 3. image

▷ 使用说明

```
python censor_tool.py image {create} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | string | 用户的公钥 |
| resource_id | string | 资源ID|
| timestamp | int64 | 时间戳信息|
| signature | string | 签名信息 |
| method | string | 图片审查任务数据输入方法，可选项{url,file}|
| scenes | string | 视频审查场景，若有多个，用","分隔，可选项{porn, politician, terror}|
| image | string | 图片内容 |
| url | string | 图片地址 |

- **create: 创建UAI视频审查任务**

  ```
  python censor_tool.py image create    --signature SIGNATURE \
                                        --public_key PUBLIC_KEY \
                                        --resource_id RESOURCE_ID \
                                        --timestamp TIMESTAMP \
                                        --method {url, file} \
                                        --scenes SCENES \
                                        [--image IMAGE] \
                                        [--url URL]
  ```

### 4. frame

▷ 使用说明

```
python censor_tool.py frame {fullcut,snapshot,query} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | string | 用户的公钥 |
| resource_id | string | 资源ID|
| timestamp | int64 | 时间戳信息|
| url | string | 视频路径 |
| signature | string | 签名信息 |
| bucket | string | 截帧图片保存的bucket |
| prefix | string | 截帧图片保存的名称前缀 |

- **fullcut: 创建UAI视频分帧任务，截取全部视频帧**

  ```
  python censor_tool.py frame fullcut   --signature SIGNATURE \
                                        --public_key PUBLIC_KEY \
                                        --resource_id RESOURCE_ID \
                                        --timestamp TIMESTAMP \
                                        --url URL \
                                        --bucket BUCKET \
                                        --prefix PREFIX
  ```

- **snapshot: 创建UAI视频分帧任务，获取视频首帧**

  ```
  python censor_tool.py frame snapshot  --signature SIGNATURE \
                                        --public_key PUBLIC_KEY \
                                        --resource_id RESOURCE_ID \
                                        --timestamp TIMESTAMP \
                                        --url URL \
                                        --bucket BUCKET \
                                        --prefix PREFIX
  ```

- **query: 查看UAI视频截帧任务状态**

  ```
  python censor_tool.py frame query --signature SIGNATURE \
                                    --public_key PUBLIC_KEY \
                                    --resource_id RESOURCE_ID \
                                    --timestamp TIMESTAMP \
                                    --job_id JOB_ID
  ```


### 5. signature

▷ 使用说明

```
python censor_tool.py signature {gen} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| config_file | string | 配置文件地址，包含基本账号信息以及资源ID |
| url | string | 文件地址 |
| job_id | int64 | 任务ID |

- **gen: 生成签名信息**

  ```
  python censor_tool.py signature gen   --config_file CONFIG_FILE \
                                        [--url URL] \
                                        [--job_id JOB_ID]
  ```



