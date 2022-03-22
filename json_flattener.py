import json

canon = json.load(open('new_skilltree_processed.json'))

def recurse_json(old_obj, count=0):
    new_obj = []
    for k, v in old_obj.items():
        v['name'] = k
        print("  "*count, k)
        if 'children' in v:
            v['children'] = recurse_json(v['children'], count+1)
        else:
            v['size'] = 3938

        new_obj.append(v)


    return new_obj

indents = ''
flat_canon = recurse_json(canon)[0]
print(flat_canon)

yml = False
if yml:
    import yaml
    yaml.dump(flat_canon, open('flat_ai_canon.yml', 'w'))

json.dump(flat_canon, open('flat_new_skilltree_processed.json', 'w'), indent=4)
