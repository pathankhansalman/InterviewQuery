def search_maze(maze_input,st_input):
    adj_dict = {}
    for i in range(len(maze_input)):
        for j in range(len(maze_input[0])):
            if maze_input[i][j] == 1:
                continue
            if (i, j) not in adj_dict:
                adj_dict[(i, j)] = []
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if abs(x + y) != 1:
                        continue
                    next_x = i + x
                    next_y = j + y
                    if next_x < 0 or next_y < 0 or next_x >= len(maze_input) or next_y >= len(maze_input[0]):
                        continue
                    if maze_input[next_x][next_y] == 0 or\
                            maze_input[next_x][next_y] == 2:
                        adj_dict[(i, j)].append((next_x, next_y))
    start = st_input
    curr_exp = set([start])
    master_curr_exp = set([start])
    curr_path = [start]
    tgt_found = False
    reset = True
    print_ct = 0
    while len(curr_path) > 0:
        if reset:
            curr_start = curr_path[-1]
            next_exp_list = [x for x in adj_dict[curr_start] if x not in master_curr_exp]
            reset = False
        next_found = False
        for i, node in enumerate(next_exp_list):
            if maze_input[node[0]][node[1]] == 2:
                curr_path.append(node)
                tgt_found = True
                break
            child_list = [x for x in adj_dict[node] if x not in curr_exp]
            master_curr_exp.add(node)
            curr_exp.add(node)
            curr_path.append(node)
            if child_list:
                next_found = True
                next_exp_list = next_exp_list[i + 1:]
                next_exp_list = [x for x in next_exp_list if x not in set(child_list)]
                next_exp_list = child_list + next_exp_list
                break
        if next_found:
            continue
        next_exp_list = []
        if tgt_found:
            break
        if not next_exp_list:
            curr_exp.remove(curr_path[-1])
            curr_path = curr_path[:-1]
            reset = True
    return curr_path