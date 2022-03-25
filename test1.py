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
                chunker_list_deep_copy = chunker_list[:]
                final_list.append(chunker_list_deep_copy)


        else:
            maximum=number
            chunker_list_deep_copy=chunker_list[:]
            final_list.append(chunker_list_deep_copy)
            chunker_list.clear()
            chunker_list.append(number)
            conter += 1
    return final_list

# print(grouped_list_maker([1,3,5,6,8,2,5,9,10,4,6,8]))
print(grouped_list_maker([1,3,2,4]))