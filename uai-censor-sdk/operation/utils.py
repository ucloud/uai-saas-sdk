def parse_unrequired_args(args, arg_name):
    if arg_name in args and args[arg_name] is not None:
        return args[arg_name]
    else:
        return ''


