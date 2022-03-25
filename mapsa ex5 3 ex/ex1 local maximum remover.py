def without_local_oporator(number_list, conter=0 ,change_num=0):

    first_element = number_list[conter]
    second_element = number_list[conter + 1]
    third_element = number_list[conter + 2]

    if len(number_list[conter:]) >= 4:
        fourth_element = number_list[conter + 3]

        if  second_element > third_element and second_element > first_element:
            if fourth_element >= second_element:
                number_list[conter + 2] = fourth_element
                change_num+=1
            elif third_element >= second_element:
                number_list[conter + 1] = third_element
                change_num+=1
            else:
                number_list[conter + 2] = second_element
                change_num+=1

        conter += 1
        return without_local_oporator(number_list, conter, change_num)

    elif len(number_list[conter:]) == 3:
        if second_element > first_element and second_element > third_element:
            # number_list[conter + 1] = third_element
            number_list[conter] = second_element
            change_num += 1
        return (number_list, change_num)


if __name__ == '__main__':

    print(without_local_oporator([2,1,2]))
    print(without_local_oporator([1,2,3,1]))
    print(without_local_oporator([1,2,1,2,1]))
    print(without_local_oporator([1,2,1,3,2,3,1,2,1]))
    print(without_local_oporator([2,1,3,1,3,1,3,1,3]))
