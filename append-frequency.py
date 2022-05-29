def inject_frequency(sentence, discard_list):
    count_dict = {}
    discard_set = set(discard_list)
    for char in sentence:
        if char in discard_set or char == ' ':
            continue
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    retval = ''
    for char in sentence:
        retval += char
        if char in discard_set or char == ' ':
            continue
        retval += str(count_dict[char])
    return retval