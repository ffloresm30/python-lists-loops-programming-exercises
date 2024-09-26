chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    combined_merge_lists = []
    for name1 in list1: 
        combined_merge_lists.append(name1)  
    for name2 in list2:
       combined_merge_lists.append(name2)  
    return combined_merge_lists

print(merge_list(chunk_one, chunk_two))
