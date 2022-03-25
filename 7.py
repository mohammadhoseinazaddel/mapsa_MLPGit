
def max_min_avg(*args):
    arg_decimaled=[]
    for arg in args:
        arg_deci=float(arg)
        arg_decimaled.append(arg_deci)
    minumem=min(arg_decimaled)
    maximum=max(arg_decimaled)
    avg=float(float(sum(arg_decimaled))/len(arg_decimaled))
    print(float(sum(arg_decimaled)))
    return (maximum,minumem,avg)
# TODO float avg
if __name__ == '__main__':
    x=1
    y=2
    z=4
    maximum,minumem,avg=max_min_avg(x,y,z)

    print(f"maximum:{maximum:.3f}\nminumem:{minumem:.3f}\navg:{avg:.3f}")
