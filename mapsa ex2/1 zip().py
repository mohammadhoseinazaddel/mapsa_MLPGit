def biger_finder(list_iter1, list_iter2):
    if len(list_iter1)>= len(list_iter2):
        return len(list_iter2)
    else:
        return len(list_iter1)


def ziper(iter1,iter2):
    list_iter1=list(iter1)
    list_iter2=list(iter2)
    len_smallest=biger_finder(list_iter1,list_iter2)
    final_list=[]
    for i in range(len_smallest):
        list1_candidate=list_iter1[0]
        list_iter1.pop(0)
        list2_candidte=list_iter2[0]
        list_iter2.pop(0)
        final_list.append((list1_candidate,list2_candidte))
    return tuple(final_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1=[1,2,3,4]
    list2=(7,9,8)
    print(ziper(list1,list2))
    # print(list(list1))
    # print(tuple(zip(list1,list2,[4,5,6])))
