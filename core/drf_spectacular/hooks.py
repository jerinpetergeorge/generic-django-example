def post_hook__add_global_header(result, generator, request, public):
    header_scheme = {
        "in": "header",
        "name": "accept-language",
        "schema": {"type": "string"},
        "description": "`fa` or `en`. The default value is en",
    }
    paths = result["paths"]
    for path, path_conf in paths.items():
        for method, method_conf in path_conf.items():
            if "parameters" in method_conf:
                method_conf["parameters"].append(header_scheme)
            else:
                method_conf["parameters"] = [header_scheme]
    return result


def pre_hook__add_global_header(endpoints):
    for (path, path_regex, method, callback) in endpoints:
        ...
    return endpoints
