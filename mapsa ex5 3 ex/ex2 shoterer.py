def number_extractor(number_Str, i, i_plus):
    plused_number = int(number_Str[i])+int(number_Str[i_plus])
    number_Str.pop(i_plus)
    number_Str[i]=str(plused_number)
    s = [str(i) for i in number_Str]
    res = int("".join(s))
    return res


def shortest_finder(number):
    number_Str = str(number)
    max_num = 0
    for i in range(0,len(number_Str)-1):

        new_number = number_extractor(list(number_Str),i,i+1)
        if new_number > max_num :
            max_num = new_number

    return max_num


if __name__ == '__main__':
    print(shortest_finder(10038))