def play_test():
    matrix = [ #задаем nonlocal матрицу 3 Х 3 с неопределенными значениями
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    memory_list = ['-', '-', '-']
    str_play = f"  0 1 2\n0 {matrix[0][0]} {matrix[0][1]} {matrix[0][2]}\n1" \
               f" {matrix[1][0]} {matrix[1][1]} {matrix[1][2]}\n2" \
               f" {matrix[2][0]} {matrix[2][1]} {matrix[2][2]}"
    print(str_play)
    def begin_play(n=0): #внутренняя функция для ввода значений Х или О в матрицу по индексам i и j
        if n == 9: #терминальное значение для рекурсивной функции (3 Х 3 = 9 значений Х или О)
            return('Game over: Боевая ничья') #как только введены все 9 значений, игра заканчивается
        print("Введите в поле крестик или нолик в виде: ijsymbol,например: 21X или 02О")
        symbol = list(input()) #ввод значений Х или О с индексами матрицы через консоль
        var_symbol, loc_i, loc_j = symbol[2], symbol[0], symbol[1]

        def change_symbol(var_symbol): #Функция проверяет, чтобы Х и О вводились попеременно и разные индексы матрицы
            if var_symbol == memory_list[2]:
                print(f"Значение {var_symbol} не может вводиться подряд. Введите противоположное значение")
                return begin_play(n) #Запускаем рекурсию для нового ввода данных при текущем счетчике n
            if loc_i == memory_list[0] and loc_j == memory_list[1]:
                print(f"Значения {loc_i} и {loc_j} указывают на занятую ячейку. Укажите одну из свободных ячеек")
                return begin_play(n)
            memory_list[0], memory_list[1], memory_list[2] = loc_i, loc_j, symbol[2]
            return None

        change_symbol(var_symbol)
        i, j = int(symbol[0]), int(symbol[1])
        matrix[i][j] = symbol[2] #Устанавливаем новое значение в матрицу

        def symbol_loc(matrix): #функция проверяет положение Х и О в ячейках и выводит результат игры
            M = set() #объявляем множества по вертикали, горизонтали и диагоналям матрицы. Нас интересует
            S = set() #момент, когда длинна элементов какого-то из них станет равна единице (либо Х либо О)
            P = set()
            R = set()
            for j in range(0, 3): #заполняем множества текущими данными из матрицы
                for i in range(0, 3):
                    M.add(matrix[j][i])
                if len(M) == 1 and '-' not in M:
                    return 'V'
                M = set()
            for i in range(0, 3):
                P.add(matrix[i][i])
                for j in range(0, 3):
                    S.add(matrix[j][i])
                if len(S) == 1 and '-' not in S:
                    return 'V'
                S = set()
            if len(P) == 1 and '-' not in P:
                return 'V'
            R.add(matrix[2][0])
            R.add(matrix[1][1])
            R.add(matrix[0][2])
            if len(R) == 1 and '-' not in R:
                return 'V'
            return 'D'

        print(f"  0 1 2\n0 {matrix[0][0]} {matrix[0][1]} {matrix[0][2]}\n1" \
              f" {matrix[1][0]} {matrix[1][1]} {matrix[1][2]}\n2" \
              f" {matrix[2][0]} {matrix[2][1]} {matrix[2][2]}")

        if symbol_loc(matrix) == 'V':
            print(f"Game over, победил {symbol[2]}")
            return 'End'
        else:
            return begin_play(n+1) #рекурсия для продолжения игры и ввода нового значения Х и О
            print('Боевая ничья')
    return begin_play()


print(play_test())









