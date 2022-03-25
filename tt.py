import random

test_list=[2,4,10,8,9,18,16]
copied_test_list=test_list
test_list.sort()
choised_list=[]
enumarated_list=enumerate(test_list)
lsited_enumarated_list=list(enumarated_list)

for i in range(2): lsited_enumarated_list.pop()


def three_min_finder(how_much_iterate):
    for i in range(how_much_iterate):
        random_choosed=random.choice(lsited_enumarated_list)
        checker(how_much_iterate,random_choosed)
        return choised_list

def checker(i,random_choosed):
    index, n = random_choosed
    index_last=0
    if len(choised_list)!=0:
        index_last, n_last = choised_list[-1]
    if len(choised_list) == 0:
        choised_list.append(random_choosed)
        i-=1
        three_min_finder(i)
    else:
        if index >= index_last:
            choised_list.append(random_choosed)
            i-=1
            three_min_finder(i)
        else:
            three_min_finder(i)
if __name__ == '__main__':
    how_much_iterate=3
    print(three_min_finder(how_much_iterate))