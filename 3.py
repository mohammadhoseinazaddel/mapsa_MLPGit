
def letter_searcher(word):
    prbable_letters=("K","C","Y","M")
    counter=0
    for letter in word:
        if letter in prbable_letters:
            counter+=1
    return counter

def probablity_finder(counter):
    probablity=pow(2,counter)
    return probablity

if __name__ == '__main__':
    print(probablity_finder(letter_searcher("CODINGBOOTCAMP")))
    print(probablity_finder(letter_searcher("MAKTABSHARIF")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
