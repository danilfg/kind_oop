import random


class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)
    
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def check_winner(self):
        for row in self.pole:
            if row[0].value == row[1].value == row[2].value:
                return (True, row[0].value)
        for col in range(3):
            if self.pole[0][col].value == self.pole[1][col].value == self.pole[2][col].value:
                return (True, self.pole[0][col].value)
        if self.pole[0][0].value == self.pole[1][1].value == self.pole[2][2].value:
            return (True, self.pole[0][0].value)
        
        if self.pole[0][2].value == self.pole[1][1].value == self.pole[2][0].value:
            return (True, self.pole[0][2].value)
        return (False, 10)
        
        
    @property
    def is_human_win(self):
        res = self.check_winner()
        if res[0] and res[1] == self.HUMAN_X:
            return True
        return False
        
    
    @property
    def is_computer_win(self):
        res = self.check_winner()
        if res[0] and res[1] == self.COMPUTER_O:
            return True
        return False
    def check_free_cell(self):
        for row in self.pole:
            for element in row:
                if element.value == self.FREE_CELL:
                    return True 
        return False
    
    def __bool__(self):
        if not self.is_computer_win and not self.is_human_win and self.check_free_cell:
            return True
        return False
    
    @property
    def is_draw(self):
        if not self.is_computer_win and not self.is_human_win and not self.check_free_cell:
            return True
        return False
    
    def __getitem__(self, item):
        if item[0] >= 3 or item[1] >= 3:
            raise IndexError('некорректно указанные индексы')
        return self.pole[item[0]][item[1]].value
        
    def __setitem__(self, key, value):
        if key[0] >= 3 or key[1] >= 3:
            raise IndexError('некорректно указанные индексы')
        if value not in (0, 1, 2):
            raise IndexError('некорректно указано значение для клетки')
        self.pole[key[0]][key[1]].value = value
        
    def init(self):
        self.__init__()
    
    def show(self):
        for row in self.pole:
            for x in row:
                print(x.value, end=' ')
            print()
            
    def human_go(self):
        row, col = input("Введите 2 числа через пробел от 0 до 2: ").split()
        self.pole[int(row)][int(col)].value = self.HUMAN_X
        
    def computer_go(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        while not bool(self.pole[row][col]):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        self.pole[row][col].value = self.COMPUTER_O
        
        
class Cell:
    def __init__(self, value=0):
        self.value = value
        
    def __bool__(self):
        return True if self.value == 0 else False
    
game = TicTacToe()
game[1, 2] = 2
game.show()
game.human_go()
game.computer_go()
game.show()
print(game[1, 2])
print(game[0, 0])
print(game[1, 0])

# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()

#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()

#     step_game += 1


# game.show()

# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")