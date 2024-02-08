def perm_palindrome(str):
    count_dict = {}
    for char in str:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    odd_found = False
    for char in count_dict:
        if count_dict[char] % 2 != 0:
            if odd_found:
                return False
            odd_found = True
    return True