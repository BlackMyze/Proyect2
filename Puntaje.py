from Siguiente_Movimiento import main
from Class.tree import Tree

def score(tree, depth=1):

    for i in main(tree, depth):
        tree.branches.append(Tree(i))

    for branch in tree.branches:
        score(branch, depth+1)

def prueba():
    t = Tree([["X","O","X"],
              ["O","X","O"],
              [" "," "," "]])

    score(t)
    print(t)

prueba()
