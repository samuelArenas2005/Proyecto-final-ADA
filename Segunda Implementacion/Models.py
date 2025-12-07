from dataclasses import dataclass
import RBTree

#Implementa la clase Equipo, usa arboles roginegros para guardar a los deportistas
class Team():

    def __init__(self, name, rbTree=RBTree.RBTree(root=None), average_performance=0, ordered_ids = []):
        self.name = name
        self.rbTree = rbTree
        self.average_performance = average_performance
        self.ordered_ids = ordered_ids
    
    def insert_sportsmen(self, sportsmen):
        for sportsman in sportsmen:
            node = RBTree.Node(
                value=sportsman.performance,
                sportsMan=sportsman
            )
            RBTree.RB_INSERT(self.rbTree, node)
    
    def cal_average_performance(self):
        total_performance = 0

        def inorder_traversal(node):
            nonlocal total_performance
            if node is not None:
                inorder_traversal(node.left)
                total_performance += node.value
                inorder_traversal(node.right)
        
        inorder_traversal(self.rbTree.root)
        
        if self.rbTree.size > 0:
            self.average_performance = total_performance / self.rbTree.size
        else:
            self.average_performance = 0

    def cal_ordered_list_ids(self):
        ordered_ids = []

        def inorder_traversal(node):
            if node is not None:
                inorder_traversal(node.left)
                ordered_ids.append(node.sportsMan.id)
                inorder_traversal(node.right)
        
        inorder_traversal(self.rbTree.root)
        self.ordered_ids = ordered_ids
    
    def get_average_performance(self):
        return self.average_performance
    
    def get_ordered_list_ids(self):
        return self.ordered_ids
    


    #Funciones Danicol
    
    def cal_max_performance(self):
        if self.rbTree.root is None:
            return None
        max_node = RBTree.TREE_MAXIMUM(self.rbTree.root)
        return max_node.sportsMan
    
    def cal_min_performance(self):
        if self.rbTree.root is None:
            return None
        max_node = RBTree.TREE_MINIMUM(self.rbTree.root)
        return max_node.sportsMan
    
    def cal_youngest_player(self):
        if self.rbTree.root is None:
            return None
        
        youngest_player = None

        def inorder_traversal(node):
            nonlocal youngest_player
            if node is not None:
                inorder_traversal(node.left)
                # Comparar edades
                if youngest_player is None or node.sportsMan.age < youngest_player.age:
                    youngest_player = node.sportsMan
                inorder_traversal(node.right)
        
        inorder_traversal(self.rbTree.root)
        return youngest_player    

    def cal_most_veteran_player(self):
        if self.rbTree.root is None:
            return None
        
        veteran_player = None

        def inorder_traversal(node):
            nonlocal veteran_player
            if node is not None:
                inorder_traversal(node.left)
                # Comparar edades
                if veteran_player is None or node.sportsMan.age > veteran_player.age:
                    veteran_player = node.sportsMan
                inorder_traversal(node.right)
        
        inorder_traversal(self.rbTree.root)
        return veteran_player   

    def cal_average_age(self):

        
        acum_age= 0

        def inorder_traversal(node):
            nonlocal acum_age
            if node is not None:
                inorder_traversal(node.left)
                acum_age += node.sportsMan.age
                inorder_traversal(node.right)
        
        inorder_traversal(self.rbTree.root)
        return acum_age/self.rbTree.size if self.rbTree.size > 0 else 0
    
    