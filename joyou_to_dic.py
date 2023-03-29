def joyou_to_dict():
    contents = ""
    all_kanjis = []
    with open('joyou.txt') as f:
        contents = f.read()
    for count,value in enumerate(contents):
        all_kanjis.append(value)
    return all_kanjis
        