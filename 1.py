
def devider(n, k):
    if k!=1:
        q,mod=divmod(n,2)
        k-=1
        n=q
        devider(n,k)
    if k==1:
        q, mod = divmod(n, 2)
        return (q,mod)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x=input("n:")
    # y=input("k:")
    # print(devider(int(x),int(y)))
    print(devider(8,3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
