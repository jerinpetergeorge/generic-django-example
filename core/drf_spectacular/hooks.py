def post_hook__add_global_header(result, generator, request, public):
    return result


def pre_hook__add_global_header(endpoints):
    for path, path_regex, method, callback in endpoints:
        ...
    return endpoints
