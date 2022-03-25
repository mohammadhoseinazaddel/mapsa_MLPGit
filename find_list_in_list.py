def grouped_list_maker(my_list):
    maximum = 1
    final_list = []
    chunker_list = []
    for number in my_list:
        if number >= maximum:
            maximum = number
            chunker_list.append(number)

        else:
            maximum = number
            final_list.append(chunker_list)
            chunker_list.clear()
            chunker_list.append(number)
    return final_list


print(grouped_list_maker([1, 3, 5, 6, 8, 2, 5, 9, 10, 4, 6, 8]))