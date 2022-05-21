#create_empty_grid -----
def create_empty_grid(n):
    G = [["-"]*n for a in range(n)]
    return G

#input_life_config ------
def input_life_config(n):
    G = create_empty_grid(n)    #Call the fucntion - create_empty_grid
    print("Please input the locations of the alive cells")
    while True:
        x, y = input().split(" ")    #User inputs the cooordiates of the living cells on the same line and the coordiates are separated by a sapce
        if int(x) == -1:    #Ternimate the while loop if x = -1
            break
        else:
            G[int(x)][int(y)]="X"    #Change the "-" to "X" according to the user's input
    return G

# count_neighbors -----
def count_neighbors(x, y, G):
    count = 0
    if x-1 >= 0 and y-1 >= 0 and G[x-1][y-1] == "X":
        count +=1

    if x-1 >= 0 and G[x-1][y] =="X":
        count +=1

    if x-1 >= 0  and y+1<=len(G)-1 and G[x-1][y+1] =="X":
        count +=1

    if x+1 <= len(G)-1 and y-1 >= 0  and G[x+1][y-1] == "X" :
        count +=1

    if x+1 <= len(G)-1  and  G[x+1][y] == "X":
        count+=1

    if x+1 <= len(G)-1 and y+1<=len(G)-1  and  G[x+1][y+1] == "X":
        count+=1 

    if y-1 >=0 and G[x][y-1] =="X":
        count +=1
            
    if y+1 <= len(G)-1 and G[x][y+1] == "X" :
        count +=1
    return count    #Return the number of neighbours of a particular cell

# update_life_config -----
def update_life_config(G):
    f =[]
    h =[]
    for a in range(len(G)):    #Create a list of x-coordinates of all cells by a for loop
        for b in range(len(G)):
            f.append(a) 

    for a in range(len(G)):    #Create a list of y-coordinates of all cells by a for loop
        for b in range(len(G)):
            h.append(b)
       
    G_list = [G for d in range(len(G)**2)]    #Create a list which contains (size of the grid) grids; e.g., if the size of a grid is 5, this lits contains 9 copies of the grid in total.

    count = list(map(count_neighbors, f, h, G_list))    #Call and apply function count_neighbors to all cells in the grid and then make it a list. This list contains all the number of neighbours of all cells.

    j = p = z = 0
    for c in G:
        for d in c:
            if d == "X":    #For living cells
                if 2 <= count[z] <= 3:    #Remains alive if the number of neighbours a cell is 2 or 3
                    pass
                else:
                    G[j][p] = "-"    #Becomes dead
            elif d == "-":    #For dead cells
                if count[z] == 3:    
                    G[j][p] = "X"    #A dead cell becomes alive if the number of neighbours a cell is 3
                else:    #Becomes alive
                    pass    #Remain dead
            p += 1    #Process to the next column in the same row
            z += 1    #Process to next cell's number of neighbours
        j += 1    #Process to the next row
        p = 0    #Reset p to 0
    nextG = G
    return (nextG)


n = int(input("Input the size of the grid: "))    #User input the size of the grid

