pos_r = 0
pos_c = 3
cadena = [
    ["-", "d", "-", "-", "d"],
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
        mapa = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'd':
                    mapa.append([i,j])
            
        valor = 9999
        
        for pos in mapa:
            d = abs(pos[0]-posr) + abs(pos[1]-posc)
            if valor > d:
                valor = d
                dirty_d = pos
        
        
        # print(dirty_d[0],dirty_d[1])
        y = dirty_d[0] - posr
        x = dirty_d[1] - posc

        #print(x,y)
        if x < 0:
            print("LEFT")
        elif x > 0:
            print("RIGHT")
        elif y < 0:
            print("UP")
        else:
            print("DOWN") 


next_move(posr=pos_r,posc=pos_c,board=cadena)