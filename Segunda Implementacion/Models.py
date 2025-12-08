import RBTree
import LinkedList

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

class Site():
    def __init__(self, name, teams = LinkedList.LinkedList(), average_performance = 0):
        self.name = name
        self.teams = teams
    
    def insert_teams(self, teams):
        for team in teams:
            node = LinkedList.Node(key=team.average_performance, data=team)
            LinkedList.LIST_INSERT(self.teams, node)
        self.order_teams_by_performance()
    
    def order_teams_by_performance(self):
        LinkedList.LIST_MERGE_SORT(self.teams)
    
    def cal_average_performance(self):
        total_performance = 0

        current = self.teams.head
        while current is not None:
            total_performance += current.data.get_average_performance()
            current = current.next
        
        if self.teams.size > 0:
            self.average_performance = total_performance / self.teams.size
        else:
            self.average_performance = 0
    
    def get_average_performance(self):
        return self.average_performance
    
    def get_worst_team(self):
        if self.teams.tail is not None:
            return self.teams.tail.data
        return None
    
    def get_best_team(self):
        if self.teams.head is not None:
            return self.teams.head.data
        return None

class List_of_Sites():
    def __init__(self, sites = LinkedList.LinkedList()):
        self.sites = sites
    
    def insert_sites(self, sites):
        for site in sites:
            node = LinkedList.Node(key=site.average_performance, data=site)
            LinkedList.LIST_INSERT(self.sites, node)
        self.order_sites_by_performance()
    
    def order_sites_by_performance(self):
        LinkedList.LIST_MERGE_SORT(self.sites)