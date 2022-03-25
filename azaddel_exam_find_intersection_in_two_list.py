


def finder_list_in_list(big_list1,small_list):
    chunked_big_list=grouped_list_maker(big_list1)
    chunked_small_list=grouped_list_maker(small_list)
    print(chunked_big_list)
    # chunked_big_lis and big is like [[[1,3,5,6,8],[2,5,9,10],[4,6,8]]
    # chunked_small_lis and big is like [[1,2,3,4],[2,6,7],[9,6,7,8]]
    all_compared_listed=[]
    counter=0
    for list_big in chunked_big_list: # list_big=[1,3,5,6,8]
        proper_index_list=chunked_small_list[counter] #proper_index_list=[1,2,3,4]
        compared=comparer(list_big,proper_index_list)
        all_compared_listed.append((compared))
        counter+=1
    return all_compared_listed

def grouped_list_maker(my_list):
    maximum=1
    final_list=[]
    chunker_list=[]
    conter = 0
    for number in my_list:
        if number >= maximum:
            maximum=number
            chunker_list.append(number)
            conter+=1
            if conter == len(my_list):
                final_list.append(chunker_list)


        else:
            maximum=number
            chunker_list_deep_copy=chunker_list[:]
            final_list.append(chunker_list_deep_copy)
            chunker_list.clear()
            chunker_list.append(number)
            conter += 1
    return final_list

def comparer(list_big,list_small):
    intersectioned_list=[]
    for i in list_big:
        for j in list_small:
            if j == i :
                intersectioned_list.append(j)
    return intersectioned_list

if __name__ == '__main__':
    big_list112=[1,3,5,6,8,2,5,9,10,4,6,8,9]
    # [[1,3,5,6,8],[2,5,9,10],[4,6,8,9]]
    small_list111=[1,2,3,4,2,6,7,9,6,7,8]
    # [[1, 2, 3, 4], [2, 6, 7,9], [6, 7, 8]]
    output = finder_list_in_list(big_list112,small_list111)
    print(output)