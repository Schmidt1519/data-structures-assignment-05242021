from pi_day import Pi
from birthday_locations import Birthday
from sweepstakes import Sweepstakes
from immediate_family import ImmediateFamily
from linkedlist import LinkedList
from bst_node import BSTNode

if __name__ == '__main__':

# 1a
    pi_day_month = Pi()
    pi_day_month.month_of_pi_day()

# 1b
    birthday_locations = Birthday()
    birthday_locations.birthday_locations()

# 1c
    sweepstakes_contestants = Sweepstakes()
    sweepstakes_contestants.add_contestants()
    sweepstakes_contestants.winner()

# 2
    immediate_family = ImmediateFamily()

# 3
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
# 3a
    linked_list.add_to_beginning(50)
    linked_list.add_to_beginning(45)
# 3b
    linked_list.contains_node(30)
    linked_list.contains_node(45)
    linked_list.contains_node(50)
    linked_list.contains_node(55)
    linked_list.contains_node(52)

# 4a
    bst = BSTNode(10)
    bst.insert_node(8)
    bst.insert_node(7)
    bst.insert_node(9)
    bst.insert_node(12)
    bst.insert_node(11)
    bst.insert_node(15)

# 4b
    bst.search_for_node(8)
    bst.search_for_node(11)
    bst.search_for_node(17)
    bst.search_for_node(14)
    bst.search_for_node(15)

# bonus 1
    bst.print_inorder()

# bonus 2
    bst.print_preorder()