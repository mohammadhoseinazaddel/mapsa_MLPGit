
def counter(*args):
    color_dictionary={}
    for i in args:
        count=args.count(i)
        color_dictionary[i]=count

    dictionary_items = color_dictionary.items()
    min_all_values = min(color_dictionary.values())

    final_dic_last={}
    for key,value in dictionary_items:
        if value  == min_all_values:
            final_dic_last[key]=value
    min_sorted_min_keys=min(sorted(final_dic_last.keys()))
    print(color_dictionary)
    print(min_all_values)
    print(final_dic_last)
    print(min_sorted_min_keys)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter(3,3,6,4,8)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
