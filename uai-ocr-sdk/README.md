### UAI-Ocr SDK工具说明文档

*Install*

```
sudo python setup.py install

```

► UAI-Ocr 工具一览

| 命令子类       | 命令名称       | 命令说明            |
| ---------- | ---------- | ------------------------ |
| resource   | create      | 创建UAI审查资源 |
|            | delete      | 删除UAI审查资源 |
|			 | modifyname  | 修改资源名称信息 |
| 			 | modifymemo  | 修改资源备注信息 |
|            | modifyoss   | 修改资源oss授权信息 |
|            | list        | 获取资源列表 |
|            | listtype    | 获取资源类型列表 |
|            | listrecord  | 获取资源请求记录 |
| signature  | gen         | 生成signature |
| ocr        | idcard      | 创建身份证识别任务 |
|            | bill        | 创建票据识别任务 |

► 使用说明

```
cd tools/ocr_tool.py

python ocr_tool.py {resource,signature,ocr} ...
```
### 1. resource

▷ 使用说明

```
python ocr_tool.py resource {create,delete,modifyname,modifymemo,modifyoss,list,listrecord,listtype} ...
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

- **create: 创建UAI文字识别资源**
  ```
  python ocr_tool.py resource create    --public_key PUBLIC_KEY \
                                        --private_key PRIVATE_KEY \
                                        [--project_id PROJECT_ID] \
                                        [--region REGION] \
                                        [--zone ZONE] \
                                        --resource_types RESOURCE_TYPES \
                                        [--resource_name RESOURCE_NAME] \
                                        [--resource_memo RESOURCE_MEMO]
  ```

- **delete: 删除UAI文字识别资源**

  ```
  python ocr_tool.py resource delete    --public_key PUBLIC_KEY \
                                        --private_key PRIVATE_KEY \
                                        [--project_id PROJECT_ID] \
                                        [--region REGION] \
                                        [--zone ZONE] \
                                        --resource_id RESOURCE_ID
  ```

- **modifyname: 修改UAI文字识别资源名称**

  ```
  python ocr_tool.py resource modifyname    --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --resource_id RESOURCE_ID \
                                            --resource_name RESOURCE_NAME
  ```

- **modifymemo: 修改UAI文字识别资源备注**

  ```
  python ocr_tool.py resource modifymemo    --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --resource_id RESOURCE_ID \
                                            --resource_memo RESOURCE_MEMO
  ```

- **modifyoss: 修改UAI文字识别oss授权信息**

  ```
  python ocr_tool.py resource modifyoss     --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
                                            --resource_id RESOURCE_ID \
                                            --oss_public_key OSS_PUBLIC_KEY \
                                            --oss_private_key OSS_PRIVATE_KEY

  ```

- **list: 获取UAI文字识别资源列表**

  ```
  python ocr_tool.py resource list  --public_key PUBLIC_KEY \
                                    --private_key PRIVATE_KEY \
                                    [--project_id PROJECT_ID] \
                                    [--region REGION] \
                                    [--zone ZONE] \
                                    [--limit LIMIT] \
                                    [--offset OFFSET]
  ```

- **listtype: 获取UAI文字识别可用资源类型**

  ```
  python ocr_tool.py resource listtype  --public_key PUBLIC_KEY \
                                            --private_key PRIVATE_KEY \
                                            [--project_id PROJECT_ID] \
                                            [--region REGION] \
                                            [--zone ZONE] \
  ```

- **listrecord: 获取UAI文字识别资源使用记录信息**

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
| config_file | string | 配置文件地址，包含基本账号信息以及资源ID |
| url | string | 文件地址 |
| job_id | int64 | 任务ID |

- **gen: 生成签名信息**

  ```
  python ocr_tool.py signature gen	--config_file CONFIG_FILE \
                                    [--url URL] \
                                    [--job_id JOB_ID]
  ```


### 3. ocr

▷ 使用说明

```
python ocr_tool.py ocr {idcard, bill} ...
```

▷ 参数说明

| 参数名称 | 参数类型 | 参数说明 |
| ------- | ------ | ------- |
| public_key | string | 用户的公钥 |
| resource_id | string | 资源ID|
| timestamp | int64 | 时间戳信息|
| signature | string | 签名信息 |
| method | string | 身份证图片输入方法，可选项{url,file}|
| image | string | 图片内容 |
| url | string | 图片地址 |

- **idcard: 创建UAI-Ocr身份证识别任务**

  ```
  python ocr_tool.py ocr idcard   --signature SIGNATURE \
                                    --public_key PUBLIC_KEY \
                                    --resource_id RESOURCE_ID \
                                    --timestamp TIMESTAMP \
                                    --method {url, file} \
                                    [--image IMAGE] \
                                    [--url URL]
  ```

- **bill: 创建UAI-Ocr票据识别任务**

  ```
  python ocr_tool.py ocr bill  --signature SIGNATURE \
                                --public_key PUBLIC_KEY \
                                --resource_id RESOURCE_ID \
                                --timestamp TIMESTAMP \
                                --method {url, file} \
                                [--image IMAGE] \
                                [--url URL]
  ```

