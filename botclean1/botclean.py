pos_r = 3
pos_c = 3
cadena = [
    ["-", "d", "-", "-", "-"],
    ["-", "d", "-", "-", "-"],
    ["-", "-", "-", "d", "-"],
    ["-", "-", "-", "d", "-"],
    ["-", "-", "d", "-", "d"]
]

def next_move(posr, posc, board):
    dirty_d = []
    if board[posr][posc] == 'd':
        print("CLEAN")
    else: 
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'd':
                    dirty_d = [i,j]
                    break
            if dirty_d != []:
                break
        print(dirty_d[0],dirty_d[1])
        y = dirty_d[0] - posr
        x = dirty_d[1] - posc

        print(x,y)
        if x < 0:
            print("LEFT")
        elif x > 0:
            print("RIGHT")
        elif y < 0:
            print("UP")
        else:
            print("DOWN") 


next_move(posr=pos_r,posc=pos_c,board=cadena)