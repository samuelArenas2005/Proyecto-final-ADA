import RBTree
import LinkedList

#Implementa la clase Equipo, usa arboles roginegros para guardar a los deportistas
class Team():

    def __init__(self, name, rbTree=None, average_performance=0, ordered_ids=None):
        self.name = name
        self.rbTree = rbTree if rbTree is not None else RBTree.RBTree(root=None)
        self.average_performance = average_performance
        self.ordered_ids = ordered_ids if ordered_ids is not None else []
    
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
    
    def get_number_of_sportsmen(self):
        return self.rbTree.size
    
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
    
    

class Site():
    def __init__(self, name, teams=None, average_performance=0, total_sportsmen=0):
        self.name = name
        self.teams = teams if teams is not None else LinkedList.LinkedList()
        self.average_performance = average_performance
        self.total_sportsmen = total_sportsmen
    
    def insert_teams(self, teams):
        for team in teams:
            node = LinkedList.Node(key=team.average_performance, data=team)
            LinkedList.LIST_INSERT(self.teams, node)
        self.order_teams_by_performance()
        self.cal_number_of_sportsmen()
    
    def order_teams_by_performance(self):
        LinkedList.LIST_MERGE_SORT(self.teams)

    
    def cal_average_age_in_site(self):
        total_age = 0
        total_sportsmen = 0

        current = self.teams.head
        while current is not None:
            team = current.data
            def inorder_traversal(node):
                nonlocal total_age, total_sportsmen
                if node is not None:
                    inorder_traversal(node.left)
                    total_age += node.sportsMan.age
                    total_sportsmen += 1
                    inorder_traversal(node.right)
            inorder_traversal(team.rbTree.root)
            current = current.next
        
        return total_age / total_sportsmen if total_sportsmen > 0 else 0
    
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

    def cal_number_of_sportsmen(self):
        total_sportsmen = 0

        current = self.teams.head
        while current is not None:
            total_sportsmen += current.data.get_number_of_sportsmen()
            current = current.next
        
        self.total_sportsmen = total_sportsmen
    
    def get_number_of_sportsmen(self):
        return self.total_sportsmen
    
    def get_best_player_across_teams(self):
        best_player = None

        current = self.teams.head
        while current is not None:
            team_best = current.data.cal_max_performance()
            if best_player is None or (team_best is not None and team_best.performance > best_player.performance):
                best_player = team_best
            current = current.next
        
        return best_player
    def get_worst_player_across_teams(self):
        worst_player = None

        current = self.teams.head
        while current is not None:
            team_worst = current.data.cal_min_performance()
            if worst_player is None or (team_worst is not None and team_worst.performance < worst_player.performance):
                worst_player = team_worst
            current = current.next
        
        return worst_player
    
    
    def get_worst_team(self):
        if self.teams.tail is not None:
            return self.teams.head.data
        return None
    
    def get_best_team(self):
        if self.teams.head is not None:
            return self.teams.tail.data
        return None
    
    def get_oldest_player_across_teams(self):
        oldest_player = None

        current = self.teams.head
        while current is not None:
            team_oldest = current.data.cal_most_veteran_player()
            if oldest_player is None or (team_oldest is not None and team_oldest.age > oldest_player.age):
                oldest_player = team_oldest
            current = current.next
            print("Current team:", current.data.name if current else "None")
        
        return oldest_player
    
    def get_youngest_player_across_teams(self):
        youngest_player = None

        current = self.teams.head
        while current is not None:
            team_youngest = current.data.cal_youngest_player()
            if youngest_player is None or (team_youngest is not None and team_youngest.age < youngest_player.age):
                youngest_player = team_youngest
            current = current.next
        
        return youngest_player

class List_of_Sites():
    def __init__(self, sites=None):
        self.sites = sites if sites is not None else LinkedList.LinkedList()
    
    def insert_sites(self, sites):
        for site in sites:
            node = LinkedList.Node(key=site.average_performance, data=site)
            LinkedList.LIST_INSERT(self.sites, node)
        self.order_sites_by_performance()
    
    def order_sites_by_performance(self):
        LinkedList.LIST_MERGE_SORT(self.sites)

    def get_oldest_player_across_Sites(self):
        oldest_player = None
        current = self.sites.head
        while current is not None:
            print("current site:", current.data.name if current else "None")
            site_oldest = current.data.get_oldest_player_across_teams()
            if oldest_player is None or (site_oldest is not None and site_oldest.age > oldest_player.age):
                oldest_player = site_oldest
            current = current.next
        return oldest_player
        
    def get_youngest_player_across_Sites(self):
        youngest_player = None
        current = self.sites.head
        while current is not None:
            site_youngest = current.data.get_youngest_player_across_teams()
            if youngest_player is None or (site_youngest is not None and site_youngest.age < youngest_player.age):
                youngest_player = site_youngest
            current = current.next
        return youngest_player
    
    def cal_average_age_across_Sites(self):
        cant=0
        total_age=0
        current = self.sites.head
        while current is not None:
            current.data.cal_number_of_sportsmen()
            total_age += current.data.cal_average_age_in_site() * current.data.get_number_of_sportsmen()
            cant += current.data.get_number_of_sportsmen()
            current = current.next
        return total_age/cant if cant>0 else 0
    
    def cal_average_performance_across_Sites(self):
        total_performance = 0
        cant=0
        current = self.sites.head
        while current is not None:
            current.data.cal_average_performance()
            current.data.cal_number_of_sportsmen()
            total_performance += current.data.get_average_performance()* current.data.get_number_of_sportsmen()
            cant +=current.data.get_number_of_sportsmen()
            current = current.next
        print("Numero de jugadores total:", cant)
        return total_performance / cant if cant > 0 else 0

    
    def get_best_team_across_Sites(self):
        best_team = None
        current = self.sites.head

        print("Sites in the list:")
        LinkedList.PRINT_LINKED_LIST(self.sites)
        while current is not None:
            site_best_team = current.data.get_best_team()
            print("current site:", current.data.name if current else "None")
            print("current team performance:", site_best_team.get_average_performance() if site_best_team else "None")
            if best_team is None or (site_best_team is not None and site_best_team.get_average_performance() > best_team.get_average_performance()):
                best_team = site_best_team
            current = current.next
        return best_team
    
    def get_worst_team_across_Sites(self):
        worst_team = None
        current = self.sites.head
        while current is not None:
            site_worst_team = current.data.get_worst_team()
            if worst_team is None or (site_worst_team is not None and site_worst_team.get_average_performance() < worst_team.get_average_performance()):
                worst_team = site_worst_team
            current = current.next
        return worst_team
    
    def get_best_player_across_Sites(self):
        best_player = None
        current = self.sites.head
        while current is not None:
            site_best_player = current.data.get_best_player_across_teams()
            if best_player is None or (site_best_player is not None and site_best_player.performance > best_player.performance):
                best_player = site_best_player
            current = current.next
        return best_player
    
    def get_worst_player_across_Sites(self):
        worst_player = None
        current = self.sites.head
        while current is not None:
            site_worst_player = current.data.get_worst_player_across_teams()
            if worst_player is None or (site_worst_player is not None and site_worst_player.performance < worst_player.performance):
                worst_player = site_worst_player
            current = current.next
        return worst_player
    


