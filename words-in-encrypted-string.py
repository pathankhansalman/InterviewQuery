def extract_word(encrypted_document, n, target_word):
    chars = [chr(x + ord('A')) for x in range(26)]
    map_dict = {k: chr((ord(k) - ord('A') + n) % 26 + ord('A')) for k in chars}
    target_enc = ''.join([map_dict[x] if x in chars else x
                          for x in list(target_word)])
    # print(map_dict, target_word, target_enc)
    return encrypted_document.count(target_enc)