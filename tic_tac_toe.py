import random
import os

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("------------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("------------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_drawl(self):
        dict_win = {}

        for i in ("X", "O"):
            # Horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            # Simplifiquei a lógica aqui para ficar mais legível, usando 'or' acumulativo
            dict_win[i] = dict_win[i] or (self.board[1][0] == self.board[1][1] == self.board[1][2] == i)
            dict_win[i] = dict_win[i] or (self.board[2][0] == self.board[2][1] == self.board[2][2] == i)

            # Verticais
            dict_win[i] = dict_win[i] or (self.board[0][0] == self.board[1][0] == self.board[2][0] == i)
            dict_win[i] = dict_win[i] or (self.board[0][1] == self.board[1][1] == self.board[2][1] == i)
            dict_win[i] = dict_win[i] or (self.board[0][2] == self.board[1][2] == self.board[2][2] == i)

            # Diagonais
            dict_win[i] = dict_win[i] or (self.board[0][0] == self.board[1][1] == self.board[2][2] == i)
            dict_win[i] = dict_win[i] or (self.board[2][0] == self.board[1][1] == self.board[0][2] == i)
        
        if dict_win["X"]:
            self.done = "x"
            print("X venceu!")
            return
        elif dict_win["O"]:
            self.done = "o"
            print("O venceu!")
            return

        tem_espaco_vazio = False
        for row in self.board:
            if " " in row:
                tem_espaco_vazio = True
                break
        
        if not tem_espaco_vazio:
            self.done = "d"
            print("Empate!")

    def get_player_move(self):
        invalid_move=True

        while invalid_move:
            try:
                print("Digite a linha de seu próximo lance (0-2): ")
                x = int(input())

                print("Digite a coluna de seu próximo lance (0-2): ")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Cordenadas erradas! Use números de 0 a 2.")
                    continue # Volta para o inicio do loop

                if self.board[x][y] != " ":
                    print("Posição já preenchida.")
                    continue
            except ValueError:
                print("Por favor, digite apenas números.")
                continue
            except Exception as e:
                print(f"Erro: {e}")
                continue
            
            invalid_move = False
            
        self.board[x][y] = "X"

    def make_move(self):
        list_move = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_move.append((i, j))
            
        if len(list_move) > 0:
            x, y = random.choice(list_move)
            self.board[x][y] = "O"

# --- GAME LOOP ---
game = TicTacToe()
game.print_board()
next_game = 0

while next_game == 0:
    os.system("cls") 
    game.print_board()
    
    while game.done == "":
        game.get_player_move()
        
        game.check_win_or_drawl()
        if game.done != "":
            break
            
        game.make_move()
        
        os.system("cls")
        game.print_board()
        
        game.check_win_or_drawl()
    
    print("\nDigite 1 para sair do jogo ou qualquer tecla para jogar novamente: ")
    try:
        user_input = int(input())
        if user_input == 1:
            break
        else:
            game.reset()
    except:
        game.reset()