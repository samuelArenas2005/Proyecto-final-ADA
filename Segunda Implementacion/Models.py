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