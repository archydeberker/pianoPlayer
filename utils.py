def permute_sort_join(list1, list2):
    new_list = list(itertools.product(list1, list2))
    new_list.sort(key=lambda x: x[1])
    new_list = [x[0] + x[1] for x in new_list]

    return new_list


def black_key_detector(piano_image):
    diff_p = np.diff(piano_image.astype(np.float))

    # We're looking for 36 black keys

    x_val = 20
    down_crit = -100
    space_crit = 350
    spacer = 25
    min_distance = 23
    key_on = []
    for i in range(diff_p.shape[1]):
        if diff_p[x_val, i] < down_crit:

            if sum(abs(diff_p[x_val, i:i + spacer])) < space_crit:
                if len(key_on) > 0:
                    if i - key_on[-1] > min_distance:
                        key_on.append(i)
                else:
                    key_on.append(i)


def add_keys_to_dict(key_ids, key_locations, max_keys, key_map={}):

    for i, value in enumerate(key_ids):
        if i < max_keys - 1:
            key_map[value] = key_locations[i]
