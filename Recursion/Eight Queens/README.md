# Problem Statement
Eight Queens: Write an algorithm to print all ways of arranging eight queens on a 8x8 chess board so that none of them share the same row, column or diagonal. In this case "diagona" means all diagonals, not just two that bisect the board.

# solution
Try solution in a recursive way.

Ways to arrange 8 queens on an 8x8 board with queen at (7,3) = 
ways to ... with queens at (7,3) and (6,0) + 
ways to ... with queens at (7,3) and (6,1) + 
ways to ... with queens at (7,3) and (6,2) +
ways to ... with queens at (7,3) and (6,4) + 
ways to ... with queens at (7,3) and (6,5) + 
ways to ... with queens at (7,3) and (6,6) + 
ways to ... with queens at (7,3) and (6,7)   