def target_value_search(rotated_input, target_value):
    if len(rotated_input) <= 2:
        return rotated_input.index(target_value)
    left = 0
    right = len(rotated_input) - 1
    pivot_idx = -1
    while 1:
        if right - left <= 1:
            if rotated_input[left] > rotated_input[right]:
                pivot_idx = left
            pivot_idx = right
            break
        mid = (left + right) // 2
        if rotated_input[mid] < rotated_input[mid - 1]:
            pivot_idx = mid - 1
            break
        elif rotated_input[mid] > rotated_input[mid + 1]:
            pivot_idx = mid
            break
        else:
            if rotated_input[left] > rotated_input[mid]:
                right = mid
            else:
                left = mid
    # print(pivot_idx)
    if pivot_idx == 0 or pivot_idx == len(rotated_input) - 1:
        if target_value == rotated_input[0]:
            return 0
        left = 1
        right = len(rotated_input) - 1
        while 1:
            if right - left <= 1:
                if rotated_input[left] == target_value:
                    return left
                elif rotated_input[right] == target_value:
                    return right
                return -1
            mid = (left + right) // 2
            if rotated_input[mid] == target_value:
                return mid
            elif rotated_input[mid] > target_value:
                right = mid
            else:
                left = mid
    else:
        left = 0
        right = pivot_idx
        while 1:
            if right - left <= 1:
                if rotated_input[left] == target_value:
                    return left
                elif rotated_input[right] == target_value:
                    return right
                break
            mid = (left + right) // 2
            if rotated_input[mid] == target_value:
                return mid
            elif rotated_input[mid] > target_value:
                right = mid
            else:
                left = mid
        left = pivot_idx + 1
        right = len(rotated_input) - 1
        while 1:
            if right - left <= 1:
                if rotated_input[left] == target_value:
                    return left
                elif rotated_input[right] == target_value:
                    return right
                return -1
            mid = (left + right) // 2
            if rotated_input[mid] == target_value:
                return mid
            elif rotated_input[mid] > target_value:
                right = mid
            else:
                left = mid