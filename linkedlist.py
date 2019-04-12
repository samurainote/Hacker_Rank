
"""
Sample Input
3
16
13
7
1
2

Sample Output
16 13 1 7

Explanation
The initial linked list is 16 13 7.
We have to insert  at the position  which currently has  in it.
The updated linked list will be 16 13 1 7
"""

import sys

def LLcreater():
    n = int(input())
    vals = []
    for _ in range(n):
        vals.append(int(input()))
    num_vals = len(vals)
    linked_list = []
    for i in range(num_vals):
        if i == num_vals-1:
            current_node = Node(data=vals[i], next_node=None)
            linked_list.append(current_node)
        else:
            current_node = Node(data=vals[i], next_node=None)
            current_node.next = vals[i+1]
            linked_list.append(current_node)
    return linked_list

def LLinserter(list):
    LL = list
    insert_node = Node(data=int(input(), next_node=None))
    insert_position = int(input())
    LL.insert(insert_position, insert_node.data)
    list[insert_position-1].next = insert_node.data
    insert_node.next = list[insert_position]
    return LL

linked_list = LLcreater()
LL = LLinserter(linked_list)
for e in LL:
    sys.sys.stdout.write(str(e))
    sys.stdout.write(" ")
    sys.stdout.flush()
