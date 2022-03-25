
def oporator_function(first_num,operator,sec_num):
    if operator == "+":
        return first_num+sec_num
    if operator == "-":
        return first_num-sec_num


if __name__ == '__main__':
    print(oporator_function(1000, "+", 1))
