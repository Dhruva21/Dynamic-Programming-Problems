color = {"Black", "White", "Red", "Yellow", "Green"}

def RecursivePaintFill(screen, r, c, ocolor, ncolor):
    if r < 0 or r >= len(screen) or c < 0 or c >= len(screen):
        return False
    
    if screen[r][c] == ocolor:
        screen[r][c] = ncolor
        RecursivePaintFill(screen, r - 1, c, ocolor, ncolor) # up
        RecursivePaintFill(screen, r + 1, c, ocolor, ncolor) # down
        RecursivePaintFill(screen, r, c - 1, ocolor, ncolor) # left
        RecursivePaintFill(screen, r, c + 1, ocolor, ncolor) # right
    return True

def PaintFill(screen, r, c, ncolor):
    if screen[r][c] == ncolor:
        return False
    return RecursivePaintFill(screen, r, c, screen[r][c], ncolor)

if __name__ == "__main":
    # call paint fill function
    print("Main")