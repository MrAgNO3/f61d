from random import randint
from os import system
def game():
    def printHead(L:int):
        print(' '*(L-7) + 'Life Game v2.0' + ' '*(L-7) + '\n\n')
        print('-'*L*2 + '┐')
    printHead(20)
    print('1.Random init matrix.')
    print('2.custome init matrix(0/1).')
    ch,qt,table = -1,['q','Q','quit','Quit'],[]
    while ch != '1' and ch != '2':
        ch = input('Choose:')#choice
    if ch == '1':
        L = 0
        while L < 10 or L > 100:
            L = int(input('Input size of map[10,100]:'))
        print('--------------------------------------------')
        table = [['0' for j in range(L+2)] for i in range(L+2)]
        for i in range(L**2//3):
            table[randint(1,L)][randint(1,L)] = '1'#随机选取1/3的点，标记为存活
    elif ch == '2':
        print('Please input the 0/1 matrix:')
        table.append([' '] + list(input()) + [' '])
        for i in range(len(table[0]) - 3):
            table.append([' '] + list(input()) + [' '])
    L = len(table) - 2
    def func():
        nt = [['0' for i in range(L+2)]for i in range(L+2)]
        for i in range(1,L+1):
            for j in range(1,L+1):
                if find(i,j) == 2:#若有2个，则状态不变
                    nt[i][j] = table[i][j]
                elif find(i,j) == 3:nt[i][j] = '1'#若有3个，则为生
        return nt
    def find(x,y):#统计周围细胞
        cnt = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i == x and j == y:continue#不判断本身
                if table[i][j] == '1':cnt += 1
        return cnt#返回周围有几个细胞
    def printable():
        system('cls')
        printHead(L)
        for i in table[1:-1]:
            j = ''.join(i[1:-1]).replace('1','■')
            print(j.replace('0','  ')+'|')
        print('-'*L*2 + '┛')
        print('Press Enter to step on')
        print('hold Enter to speed up')
        print('input q to quit')
    printable()
    while input() not in qt:
        table = func()
        printable()
    a = input("Quit!!")
