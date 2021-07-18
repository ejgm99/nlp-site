
#"flattens" a json object from a dictionary into something that makes more
#sense from a template rendering standpoint
def jsonToHTML(json_object):
    keys = list(json_object.keys())
    json_list = []
    for i in range(len(json_object[keys[0]])):
        temp_dict = {}
        for key in keys:
            temp_dict[key] = json_object[key][str(i)]
        json_list.append(temp_dict)
    return json_list
