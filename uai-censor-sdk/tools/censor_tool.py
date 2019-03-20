import argparse
from operation.create_image_censor_job_op import UAICensorCreateImageJobOp
from operation.create_video_censor_job_op import UAICensorCreateVideoJobOp
from operation.get_video_censor_job_op import UAICensorGetVideoCensorJobOp
from operation.create_video_to_frame_first_view_job_op import UAICensorCreateVideoToFrameFirstViewJobOp
from operation.create_video_to_frame_full_cut_job_op import UAICensorCreateVideoToFrameFullCutJobOp
from operation.get_video_to_frame_job_op import UAICensorGetVideoToFrameJobOp
from operation.gen_job_signature_op import UAICensorGenJobSignatureOp

from operation.create_censor_resource_op import CreateCensorResourceOp
from operation.delete_censor_resource_op import DeleteCensorResourceOp
from operation.modify_censor_resource_name_op import ModifyUAICensorResourceNameOp
from operation.modify_censor_resource_memo_op import ModifyUAICensorResourceMemoOp
from operation.modify_censor_resource_oss_op import ModifyUAICensorResourceOssOp
from operation.get_censor_resource_list_op import GetUAICensorResourceListOp
from operation.get_censor_resource_record_info_op import GetUAICensorResourceRecordInfoOp
from operation.get_avail_censor_resource_type_op import GetUAICensorAvailCensorResourceTypeOp


def parse_args(subparser):
    resource_parser = subparser.add_parser('resource', help='resource concerned tools')
    resource_tool_parser = resource_parser.add_subparsers(dest='action_name', help='action name')
    create_resource_parser = resource_tool_parser.add_parser('create', help='create uai censor resource')
    delete_resource_parser = resource_tool_parser.add_parser('delete', help='delete uai censor resource')
    modify_resource_name_parser = resource_tool_parser.add_parser('modifyname', help='modify resource name')
    modify_resource_memo_parser = resource_tool_parser.add_parser('modifymemo', help='modify resource memo')
    modify_resource_oss_parser = resource_tool_parser.add_parser('modifyoss', help='modify resource oss info')
    list_resource_parser = resource_tool_parser.add_parser('list', help='list uai censor resources of current user')
    list_resource_record_parser = resource_tool_parser.add_parser('listrecord', help='list resource record infos')
    list_resource_type_parser = resource_tool_parser.add_parser('listtype', help='list available censor resource types')

    video_parser = subparser.add_parser('video', help='video concerned tools')
    video_tool_parser = video_parser.add_subparsers(dest='action_name', help='action name')
    create_video_job_parser = video_tool_parser.add_parser('create', help='create video censor job')
    query_video_job_parser = video_tool_parser.add_parser('query', help='get video censor job info')

    image_parser = subparser.add_parser('image', help='image concerned tools')
    image_tool_parser = image_parser.add_subparsers(dest='action_name', help='action name')
    create_image_job_parser = image_tool_parser.add_parser('create', help='create image censor job')

    frame_parser = subparser.add_parser('frame', help='frame concerned tools')
    frame_tool_parser = frame_parser.add_subparsers(dest='action_name', help='action name')
    create_toframe_fullcut_job_parser = frame_tool_parser.add_parser('fullcut', help='create video toframe job, with fullcut mode')
    create_toframe_firstview_job_parser = frame_tool_parser.add_parser('snapshot', help='create video toframe job, with snapshot mode')
    query_toframe_job_parser = frame_tool_parser.add_parser('query', help='query video toframe job')

    signature_parser = subparser.add_parser('signature', help='signature concerned tools')
    signature_tool_parser = signature_parser.add_subparsers(dest='action_name', help='action name')
    gen_signature_parser = signature_tool_parser.add_parser('gen', help='gen signature for video/image job')

    create_video_job_op = UAICensorCreateVideoJobOp(create_video_job_parser)
    query_video_job_op = UAICensorGetVideoCensorJobOp(query_video_job_parser)
    create_image_job_op = UAICensorCreateImageJobOp(create_image_job_parser)
    create_toframe_first_view_job_op = UAICensorCreateVideoToFrameFirstViewJobOp(create_toframe_firstview_job_parser)
    create_toframe_fullcut_job_op = UAICensorCreateVideoToFrameFirstViewJobOp(create_toframe_fullcut_job_parser)
    query_toframe_job_op = UAICensorGetVideoToFrameJobOp(query_toframe_job_parser)
    gen_signature_op = UAICensorGenJobSignatureOp(gen_signature_parser)

    create_resource_op = CreateCensorResourceOp(create_resource_parser)
    delete_resource_op = DeleteCensorResourceOp(delete_resource_parser)
    modify_resource_oss_op = ModifyUAICensorResourceOssOp(modify_resource_oss_parser)
    modify_resource_name_op = ModifyUAICensorResourceNameOp(modify_resource_name_parser)
    modify_resource_memo_op = ModifyUAICensorResourceMemoOp(modify_resource_memo_parser)
    list_resource_op = GetUAICensorResourceListOp(list_resource_parser)
    list_resource_record_op = GetUAICensorResourceRecordInfoOp(list_resource_record_parser)
    list_resource_type_op = GetUAICensorAvailCensorResourceTypeOp(list_resource_type_parser)

    video_op_dic = {
        'create': create_video_job_op,
        'query': query_video_job_op,
    }

    image_op_dic = {
        'create': create_image_job_op,
    }

    frame_op_dic = {
        "fullcut": create_toframe_fullcut_job_op,
        "query": query_toframe_job_op,
        "snapshot": create_toframe_first_view_job_op,
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
        "video": video_op_dic,
        "image": image_op_dic,
        "resource": resource_op_dic,
        "frame": frame_op_dic,
        "signature": signature_op_dic,
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
        description='UAI Censor SDK Tools Commander',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparser = parser.add_subparsers(dest='commands', help='commands')

    cmd_op_dic = parse_args(subparser)
    cmd_args = param_filter(vars(parser.parse_args()))
    cmd_op_dic.get(cmd_args['commands']).get(cmd_args['action_name']).cmd_run(cmd_args)
