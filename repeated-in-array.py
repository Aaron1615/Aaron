def duplicate_items(list_numbers):
    """Finds repeated items in a list (list_numbers and returns them in sorted order"""
    sort_list = sorted(list_numbers)
    current_num = sort_list[0]
    items = []
    in_items = False
    for i in range(1,len(sort_list)):
        if current_num == sort_list[i] and not in_items:
            items.append(current_num)
            in_items = True
        elif current_num != sort_list[i]:
            in_items = False
            current_num = sort_list[i]
            
    return items
