

def _selfmul(x):
    temp = 1
    for i in range(1,x+1):
        temp*=i
    return temp

def fun(n,m):
    if n == m:
        return 1
    y1 = _selfmul(n)
    y2 = _selfmul(m)
    y3 = _selfmul(n-m)
    return (y1/(y2*y3))/2


def recursion(n):
    x=0
    global count1
    if n > 0:
        n -= 1
        lst.append(0)
        recursion(n)
        lst.pop()
        lst.append(1)
        recursion(n)
        lst.pop()
    else:
        for i in lst:
            if i==1:
                x+=1
        if x==count:  #修改count可以得出k权重的向量

            #print(lst,end='  ')
            x1= lst[0]
            x2 = lst[1]
            x3 = lst[2]
            x4 = lst[3]
            # x5 = lst[4]
            # x6 = lst[5]
            # x7 = lst[6]
            # x8 = lst[7]
            # x9 = lst[8]
            # x10 = lst[9]
            # x11 = lst[10]
            # x12 = lst[11]
            # x13 = lst[12]
            # x14 = lst[13]
            # x15 = lst[14]
            # x16 = lst[15]
            # x17 = lst[16]
            # x18 = lst[17]
            # x19 = lst[18]
            # x20 = lst[19]
            # x21 = lst[20]
            # x22 = lst[21]
            # x23 = lst[22]
            # x24 = lst[23]
            # x25 = lst[24]
            # x26 = lst[25]
            # x27 = lst[26]
            # x28 = lst[27]
            # x29 = lst[28]
            # x30 = lst[29]
            # x31 = lst[30]
            # x32 = lst[31]


            # please input ANF of Boolean function
            a2 = x1 + x2 + x1 * x2 + x1 * x3 + x2 * x3 + x1 * x2 * x3 + x1 * x3 * x4
            a = a2
            if a%2==0:
                #print('0')
                lst1.append(0)
            else:
                print(lst)
                lst1.append(1)
                count1 += 1



if __name__ == '__main__':
    while 1:
        n = int(input('输入元数:'))
        count = int(input('请输入重量k:'))
        ret = fun(n,count)
        count1 = 0
        lst = []
        lst1 = []
        recursion(n)
        # print(lst1)
        print('1的个数为%d(实际)' % count1)
        print('1的个数为%d(应该)' % ret)

