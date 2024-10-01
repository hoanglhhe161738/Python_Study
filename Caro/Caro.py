import random
from tabnanny import check
from turtle import delay
grid = [0,1,2,3,4,5,6,7,8]
def print_grid():
    for i in range(0, 9, 3):
        print('|', end='')
        for j in range(i, i+3):
            print(grid[j], end=' ')
        print('|')
        if i != 6:
            print('-+-+-+-+')
print_grid()

def available_Cell():
    for i in range(9):
        if grid[i] != 'X' and grid[i] != 'O':
            return True
def check(variable,x1, x2, x3):
    if grid[x1] == variable and grid[x2] == variable and grid[x3] == variable:
        return True
    return False
def check_win(variable):
    if check(variable,0,1,2) or check(variable,3,4,5) or check(variable,7,8,9) or check(variable,0,3,6) or check(variable,1,4,7) or check(variable,2,5,8) or check(variable,0,4,8) or check(variable,2,4,6):
        return True
    return False

while available_Cell():
    flag_human = False
    human = int (input('Đến lượt bạn, bạn chọn ô nào :'))
    if flag_human != True:
        if grid[human] == 'X' or grid[human] == 'O':
                print('Ô đã đánh, bạn phải chọn ô khác.')
        else:
            grid[human] = 'X'
            flag_human = True
    if flag_human != False:
        pass
    AI = random.randint(0, 8)
    if grid[AI] == 'X' or grid[AI] == 'O':
        pass
    else:
        grid[AI] = 'O'
        print_grid()
        flag_computer = False
    if flag_computer != False:
        pass
        print_grid()
    if check_win('X'):
        win = 'Bạn'
        break
    if check_win('O'):
        win = 'Computer'
        break
if win == '':
    print('Hòa!')
else:
    print(win, 'đã chiến thắng!')
