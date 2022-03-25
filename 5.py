
def reverse_checker(number):
    reversed=str(number)[::-1]
    if int(reversed)==number:
        return "yes"
    return "no"
    # r = 0
    # while number > 0:
    #     r *= 10
    #     r += number % 10
    #     number /= 10
    # return r


if __name__ == '__main__':
    print(reverse_checker(1537351))
