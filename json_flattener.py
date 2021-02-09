import json

canon = json.load(open('ai_canon.json'))

def recurse_json(old_obj):
    new_obj = []
    for k, v in old_obj.items():
        v['name'] = k
        if 'children' in v:
            v['children'] = recurse_json(v['children'])
        else:
            v['size'] = 3938

        new_obj.append(v)


    return new_obj

flat_canon = recurse_json(canon)[0]
print(flat_canon)
json.dump(flat_canon, open('flat_ai_canon.json', 'w'), indent=4)
