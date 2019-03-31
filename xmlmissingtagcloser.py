import uuid
import re


def close_missing_tags(boom, close_tag):
    if boom[-1] == close_tag.replace('/', ''):
        boom.pop()
        return close_tag
    else:
        missing_tag = '</'+boom[-1][1:]
        print('HIER MIST: '+missing_tag)
        boom.pop()
        return missing_tag + (close_missing_tags(boom, close_tag))


boom = []
f = open('naam1.xml', 'r')
fixed = open(str(uuid.uuid4())+'.xml', 'w')
for line in f:
    print(line)
    tags = re.findall('<[a-zA-Z1-9/ ="\']*>', line, 0)
    # print(tags)
    for tag in tags:
        # print('TAG:'+tag)
        if '/>' in tag:
            continue
        elif '/' in tag:
            endTags = close_missing_tags(boom, tag)
            line = line.replace(tag, endTags)
        else:
            # attributen weglaten, tot 1e spatie dus
            tag = tag.split(' ')[0]+'>' if ' ' in tag else tag
            boom.append(tag)
    fixed.write(line)

