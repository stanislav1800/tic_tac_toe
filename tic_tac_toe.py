def check_move(moves):#Проверка входных данных
    if option==1 and 1<=int(moves)<=9:
        i=0
        for row in range(3):
            for col in range(3):
                i += 1
                if i==int(moves)and not playing_positions[row][col]:
                    playing_positions[row][col] = players[0][move % 2]
                    return
        return 'error'
    if not ' ' in moves  or moves[-1]==' ' or moves[0]==' ':
        return 'error'
    i1, i2 = moves.split()
    if not 1<=int(i1)<=3 or not 1<=int(i2)<=3:
        print('Ход за пределами поля')
        return 'error'
    if not playing_positions[int(i1) - 1][int(i2) - 1]:
        playing_positions[int(i1) - 1][int(i2) - 1] = players[0][move % 2]
    else:
        print('Поле занято')
        return 'error'
    return
def field_output():#Вывод поля игры
    if option==1:
        i=0
        for row in range(3):
            s = ' '
            for col in range(3):
                i+=1
                if playing_positions[row][col]:
                    s += playing_positions[row][col] + ' '
                else:
                    s +=str(i)+' '
            print(s)
        return
    print('  1 2 3')
    for row in range(3):
        s = str(row+1)+' '
        for col in range(3):
            if playing_positions[row][col]:
                s+=playing_positions[row][col]+' '
            else:
                s += playing_positions[row][col] + '- '
        print(s)
def check_win():#Проверка выйгрыша и ничьей
    for i in range(8):
        k1 = 0
        k = 0
        for row in range(3):
            for col in range(3):
                if playing_positions[row][col] :
                    k1+=1
                if playing_positions[row][col] and winning_positions[i][row][col] and playing_positions[row][col] == players[0][move % 2]:
                    k += 1
        if k==3:
            players[1][move % 2]+=1
            print(f'Победил Игрок {move % 2+1} ')
            print(f'Счет! \nИгрок 1 - {players[1][0]}: Игрок 2 - {players[1][1]} ')
            if input('Выйти(1) Начать занаво(2)')=='2':
                return 2
            else: return 1
    if k1==9:
        print('Ничья')
        print(f'Счет! \nИгрок 1 - {players[1][0]}:Игрок 2 - {players[1][1]} ')
        if input('Выйти(1) Начать занаво(2)') == '2':
            return 2
        else:
            return 1

winning_positions=[[['w','w','w'],['','',''],['','','']],
                   [['','',''],['w','w','w'],['','','']],
                   [['','',''],['','',''],['w','w','w']],
                   [['w','',''],['w','',''],['w','','']],
                   [['','w',''],['','w',''],['','w','']],
                   [['','','w'],['','','w'],['','','w']],
                   [['w','',''],['','w',''],['','','w']],
                   [['','','w'],['','w',''],['w','','']]]
playing_positions=[['','',''],['','',''],['','','']]
players=[['x','o'],[0,0]]
move=0
option=0
if input("Правила игры: Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). "
         "Первый, выстроивший в ряд 3 своих фигуры выигрывает. Если игроки заполнили все 9 ячеек партия считается закончившейся в ничью. "
         "\nВ свой ход надо ввести два числа от 1 до 3 через пробел. \nПример:1 3 \n  1 2 3\n1 - - x\n2 - - -\n3 - - - \nДля сманы игрового поля введите 1\n")=="1":
    input('В свой ход надо ввести число от 1 до 9\nПример:5 \n  1 2 3\n  4 x 6\n  7 8 9\n')
    print('\n'*10)
    option=1
field_output()
while True:
    if check_move(input(f'Ход Игрока {move % 2+1} :'))=='error':
        continue
    field_output()
    check=check_win()
    if check==1:
        break
    elif check==2:
        playing_positions = [['', '', ''], ['', '', ''], ['', '', '']]
        field_output()
        move += 1
        continue
    move += 1

print('End')