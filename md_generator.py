import json

canon = json.load(open('ai_canon.json'))
markdown = open('ai_canon.md', 'w')
markdown.write('# AI Canon\n')

def recurse_json(old_obj, depth=0):
    new_obj = []
    for k, v in old_obj.items():
        markdown.write(f'{"  "*depth}* {k}\n')
        if 'children' in v:
            d = depth + 1
            recurse_json(v['children'], d)   


    return new_obj

md_canon = recurse_json(canon)
print(md_canon)
