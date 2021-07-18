import emoji

emoji_dict = {
    "0":":joy:",
    "1":":unamused:",
    "2":":weary:",
    "3":":sob:",
    "4":":heart_eyes:",
    "5":":pensive:",
    "6":":ok_hand:",
    "7":":blush:",
    "8":":heart:",
    "9":":smirk:",
    "10":":grin:",
    "11":":notes:",
    "12":":flushed:",
    "13":":100:",
    "14":":sleeping:",
    "15":":relieved:",
    "16":":relaxed:",
    "17":":raised_hands:",
    "18":":two_hearts:",
    "19":":expressionless:",
    "20":":sweat_smile:",
    "21":":pray:",
    "22":":confused:",
    "23":":kissing_heart:",
    "24":":heart:",
    "25":":neutral_face:",
    "26":":information_desk_person:",
    "27":":disappointed:",
    "28":":see_no_evil:",
    "29":":weary:",
    "30":":v:",
    "31":":sunglasses:",
    "32":":rage:",
    "33":":thumbsup:",
    "34":":cry:",
    "35":":sleepy:",
    "36":":yum:",
    "37":":triumph:",
    "38":":hand:",
    "39":":mask:",
    "40":":clap:",
    "41":":eyes:",
    "42":":gun:",
    "43":":persevere:",
    "44":":smiling_imp:",
    "45":":sweat:",
    "46":":broken_heart:",
    "47":":green_heart:",
    "48":":musical_note:",
    "49":":speak_no_evil:",
    "50":":wink:",
    "51":":skull:",
    "52":":confounded:",
    "53":":smile:",
    "54":":stuck_out_tongue_winking_eye:",
    "55":":angry:",
    "56":":no_good:",
    "57":":muscle:",
    "58":":punch:",
    "59":":purple_heart:",
    "60":":sparkling_heart:",
    "61":":blue_heart:",
    "62":":grimacing:",
    "63":":sparkles:"
}

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

def emojize_labels(json_list):
    for entry in json_list:
        entry['labels'] = [emoji.emojize( emoji_dict[str(label)] , use_aliases=True ) for label in entry['labels'] ]
    return json_list

def handleResponse(json_object):
    json_list = emojize_labels(jsonToHTML(json_object))
    return json_list
