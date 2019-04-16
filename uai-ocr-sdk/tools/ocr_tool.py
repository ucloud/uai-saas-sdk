import argparse
from operation.gen_job_signature_op import UAIOcrGenJobSignatureOp
from operation.create_ocr_idcard_job_op import CreateUAIOcrIdcardJobOp
from operation.create_ocr_bill_job_op import CreateUAIOcrBillJobOp

from operation.create_ocr_resource_op import CreateOcrResourceOp
from operation.delete_ocr_resource_op import DeleteOcrResourceOp
from operation.modify_ocr_resource_name_op import ModifyUAIOcrResourceNameOp
from operation.modify_ocr_resource_memo_op import ModifyUAIOcrResourceMemoOp
from operation.modify_ocr_resource_oss_op import ModifyUAIOcrResourceOssOp
from operation.get_ocr_resource_list_op import GetUAIOcrResourceListOp
from operation.get_ocr_resource_record_info_op import GetUAIOcrResourceRecordInfoOp
from operation.get_avail_ocr_resource_type_op import GetUAIOcrAvailOcrResourceTypeOp


def parse_args(subparser):
    resource_parser = subparser.add_parser('resource', help='resource concerned tools')
    resource_tool_parser = resource_parser.add_subparsers(dest='action_name', help='action name')
    create_resource_parser = resource_tool_parser.add_parser('create', help='create uai ocr resource')
    delete_resource_parser = resource_tool_parser.add_parser('delete', help='delete uai ocr resource')
    modify_resource_name_parser = resource_tool_parser.add_parser('modifyname', help='modify resource name')
    modify_resource_memo_parser = resource_tool_parser.add_parser('modifymemo', help='modify resource memo')
    modify_resource_oss_parser = resource_tool_parser.add_parser('modifyoss', help='modify resource oss info')
    list_resource_parser = resource_tool_parser.add_parser('list', help='list uai ocr resources of current user')
    list_resource_record_parser = resource_tool_parser.add_parser('listrecord', help='list resource record infos')
    list_resource_type_parser = resource_tool_parser.add_parser('listtype', help='list available ocr resource types')

    ocr_parser = subparser.add_parser('ocr', help='ocr concerned tools')
    ocr_tool_parser = ocr_parser.add_subparsers(dest='ocr type', help='ocr type name')
    ocr_idcard_parser = ocr_tool_parser.add_parser('idcard', help='create idcard ocr job')
    ocr_bill_parser = ocr_tool_parser.add_parser('bill', help='create bill ocr job')

    signature_parser = subparser.add_parser('signature', help='signature concerned tools')
    signature_tool_parser = signature_parser.add_subparsers(dest='action_name', help='action name')
    gen_signature_parser = signature_tool_parser.add_parser('gen', help='gen signature for video/image job')

    gen_signature_op = UAIOcrGenJobSignatureOp(gen_signature_parser)

    create_resource_op = CreateOcrResourceOp(create_resource_parser)
    delete_resource_op = DeleteOcrResourceOp(delete_resource_parser)
    modify_resource_oss_op = ModifyUAIOcrResourceOssOp(modify_resource_oss_parser)
    modify_resource_name_op = ModifyUAIOcrResourceNameOp(modify_resource_name_parser)
    modify_resource_memo_op = ModifyUAIOcrResourceMemoOp(modify_resource_memo_parser)
    list_resource_op = GetUAIOcrResourceListOp(list_resource_parser)
    list_resource_record_op = GetUAIOcrResourceRecordInfoOp(list_resource_record_parser)
    list_resource_type_op = GetUAIOcrAvailOcrResourceTypeOp(list_resource_type_parser)

    ocr_idcard_job_op = CreateUAIOcrIdcardJobOp(ocr_idcard_parser)
    ocr_bill_job_op = CreateUAIOcrBillJobOp(ocr_bill_parser)

    ocr_op_dic = {
        "idcard": ocr_idcard_job_op,
        "bill": ocr_bill_job_op,
    }

    signature_op_dic = {
        "gen": gen_signature_op
    }

    resource_op_dic = {
        "create": create_resource_op,
        "delete": delete_resource_op,
        "modifyoss": modify_resource_oss_op,
        "modifyname": modify_resource_name_op,
        "modifymemo": modify_resource_memo_op,
        "list": list_resource_op,
        "listrecord": list_resource_record_op,
        "listtype": list_resource_type_op
    }

    cmd_op_dic = {
        "resource": resource_op_dic,
        "signature": signature_op_dic,
        "ocr": ocr_op_dic,
    }

    return cmd_op_dic


def param_filter(params):
    res_params = {}
    for key in params:
        if params[key] is not None:
            res_params[key] = params[key]
    return res_params


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='UAI Ocr SDK Tools Commander',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparser = parser.add_subparsers(dest='commands', help='commands')

    cmd_op_dic = parse_args(subparser)
    cmd_args = param_filter(vars(parser.parse_args()))
    cmd_op_dic.get(cmd_args['commands']).get(cmd_args['action_name']).cmd_run(cmd_args)
