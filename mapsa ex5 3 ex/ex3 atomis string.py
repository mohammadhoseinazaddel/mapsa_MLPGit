def change_question_mark(str_list, conter):

    if str_list[conter-1] == "0":
        str_list[conter] = "1"
        return str_list
    elif str_list[conter-1] == "1":
        str_list[conter] = "0"
        return str_list
    else:
        # if all(str_list.members == "?"):
        #     return True
        str_list[conter] = "0"
        return str_list



def str_checker(str_list):
    s = [str(i) for i in str_list]
    res = str("".join(s))
    if (res.find("11") and res.find("00")) == -1:
        return True
    else:
        return False



def well_defined_finder(str_given):
    str_list=list(str_given)

    if str_list[0] == "?":
        str_list.reverse()

    conter=0
    for i in str_list:
        if i == "?":
            str_list=change_question_mark(str_list, conter)
            conter += 1
        else:
            conter+=1

    return str_checker(str_list)




if __name__ == '__main__':
    print("is '0??10' well defined : ",well_defined_finder("0??10"))
    print("is '1?0' well defined : ",well_defined_finder("1?0"))
    print("is '???' well defined : ",well_defined_finder("???"))
    print("is '0??0' well defined : ",well_defined_finder("0??0"))
    # print(well_defined_finder("0???0"))
    # print(well_defined_finder("?0"))

