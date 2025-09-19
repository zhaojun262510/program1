def remove_duplicates(lst):
    seen = set()
    unique_lst = []
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

print(remove_duplicates([1, 2, 3, 2, 1, 4, 5]))  # 输出：[1, 2, 3, 4, 5]