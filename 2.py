import re

def date_changer(date):
    date_list=re.findall('..', date)
    saal=date_list[0]
    mah=date_list[1]
    ruz=date_list[2]
    return (saal,mah,ruz)


if __name__ == '__main__':
    saal,mah,ruz=date_changer("000107")
    print(f"saal:{saal}\nmaah:{mah}\nrooz:{ruz}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
