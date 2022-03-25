

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
            if number==my_list[-1]:
                final_list.append([number])
            conter += 1
    print(final_list)
    return len(final_list)

if __name__ == '__main__':
    big_list112=[1,3,5,6,8,2,5,9,10,4,6,8,9]
    # [[1,3,5,6,8],[2,5,9,10],[4,6,8,9]]
    small_list111=[1,5,8,12,6,15,21,42,13]
    # [[1, 2, 3, 4], [2, 6, 7,9], [6, 7, 8]]
    # output = grouped_list_maker(big_list112)
    output2 = grouped_list_maker(small_list111)
    # print(output)
    print(output2)