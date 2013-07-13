''' Building a binary tree in Python and performing various types of traversals on it. '''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
def insert( tree, data ):
    if tree==None:
        tree = Node(data)
        return tree
    if( data <= tree.data ):
        tree.left = insert( tree.left, data )
    else:
        tree.right = insert( tree.right, data )
    return tree

def inorder( tree ):
    if tree != None:
        for root in inorder( tree.left ):
            yield root
        yield tree.data
        for root in inorder( tree.right ):
            yield root            

def preorder( tree ):
    if tree != None:
        yield tree.data
        for root in preorder( tree.left ):
            yield root
        for root in preorder( tree.right ):
            yield root

def postorder( tree ):
    if tree != None:
        for root in postorder( tree.left ):
            yield root
        for root in postorder( tree.right ):
            yield root
        yield tree.data
        
def levelorder( tree ):
    if tree != None:
        treeLevelNodes, nodesInLevel = [], []
        nodesInLevel.append( tree )
        treeLevelNodes.append( nodesInLevel )
        for level,nodeList in enumerate(treeLevelNodes):
            nodesInLevel= []
            for root in nodeList:
                yield (level, root.data)
                if root.left:
                    nodesInLevel.append( root.left )
                if root.right:
                    nodesInLevel.append( root.right )
            if( len(nodesInLevel) ):
                treeLevelNodes.append(nodesInLevel)

            
if __name__ == '__main__':
    t = Node( 2 )
    insert( t, 5 )
    insert( t, 6 )
    insert( t, 1 )
    insert( t, 4 )
    
    print 'Inorder Traversal'
    for i in inorder( t ):
        print '%d, '%i,
        
    print '\nPreorder Traversal'
    for p in preorder( t ):
        print '%d, '%p,
        
    print '\nPostorder Traversal'
    for p in postorder( t ):
        print '%d, '%p,
        
    print '\nLevelorder Traversal'
    prevLevel = 0
    for level, ldata in levelorder( t ):
        if prevLevel!=level:
            print
            prevLevel = level
        print '%d, '%(ldata),
