from tqdm import trange
from time import sleep
from random import randint
from os import system

import f61d.LOGO as LOGO

print(LOGO.randlogo())
print("Welcome to F61D")

help_cont = {}
help_cont[0] = 'help     : See this help page'
help_cont[1] = 'fuckstar : One Button to fuck Satellite'
help_cont[2] = 'lifeGame : Play the Life Game'
help_cont[3] = 'paint    : Draw a Bing Dwen Dwen'
help_cont[4] = 'b64tofile: Decode base64 to a file'
help_cont[5] = 'func5'


def help(page=1,lines = 5):
    maxPage = len(help_cont)//lines
    if (page - 1) * lines >= len(help_cont):
        aprint(f'Page Error, check the number : [{1},{maxPage}]')
        return
    print(f"{'=-'*14}= H E L P {'=-'*14}=\n")
    for i in range(lines):
        n = i+lines*(page-1)
        print(f"   {n} - {help_cont[n]}")
    print(f"\n{'=-'*14} page({page}/{maxPage}) {'-='*14}")
    if page < maxPage:print(f'\t\t\thelp({page+1}) for next page')


def fuckStar():
    print('欢迎使用一键日卫星功能')
    print('请输入要日的卫星编号(可在官网查询):',end='')
    num = input()
    while num == '':
        num = input('请重新输入：')
    for i in trange(randint(1000,2000)):
        for _ in range(66666):
            a = 1
            b = 1
            a,b = b,1
    for i in range(3):
        print('.',end='')
        sleep(0.4)
    print('\n日卫星失败，请重新尝试')
    
def lifeGame():
    from f61d.lifeGame import game
    game()
    
def paint():
    from f61d.bingdwendwen import draw
    draw()
    
def b64tofile():
    menu = '''
please choose mode (1/2):
    - 1. encode
        Base64 encode a file
    - 2. decode
        Base64 decode a file
'''
    mode = input(menu)
    f1 = input('input file name:')
    f2 = input('Output file name:')
    while mode not in ['1','2']:
        mode = input('Please choose mode (1/2):')
    f = open(f1,'rb').read()
    from base64 import b64decode,b64encode
    if mode == '1':
        df = b64decode(f)
    elif mode == '2':
        df = b64encode(f)
    with open(f2,'wb') as ff:
        ff.write(df)
    
def func5():
    print('func5')

def main():
    b64tofile()

if __name__ == '__main__':
    main()
