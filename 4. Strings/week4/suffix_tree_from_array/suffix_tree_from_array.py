# python3
import sys
import threading

class SuffixTreeNode:
    def __init__(self, parent=None, children=None, string_depth=0, edge_start=-1, edge_end=-1):
        self.parent = parent
        self.children = children if children else {}
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end

def create_new_leaf(node, s, suffix):
    leaf = SuffixTreeNode(parent=node, string_depth=(len(s) - suffix),
                          edge_start=(suffix + node.string_depth),
                          edge_end=(len(s) - 1))
    node.children[s[leaf.edge_start]] = leaf
    return leaf

def break_edge(node, s, start, offset):
    start_char = s[start]
    mid_char = s[start + offset]
    mid_node = SuffixTreeNode(parent=node, string_depth=(node.string_depth + offset),
                              edge_start=start, edge_end=(start + offset - 1))
    mid_node.children[mid_char] = node.children[start_char]
    node.children[start_char].parent = mid_node
    node.children[start_char].edge_start += offset
    node.children[start_char] = mid_node
    return mid_node

def stf_from_sa(s, order, lcp_array):
    root = SuffixTreeNode()
    lcp_prev = 0
    cur_node = root
    for i in range(len(s)):
        suffix = order[i]
        while cur_node.string_depth > lcp_prev:
            cur_node = cur_node.parent
        if cur_node.string_depth == lcp_prev:
            cur_node = create_new_leaf(cur_node, s, suffix)
        else:
            edge_start = order[i - 1] + cur_node.string_depth
            offset = lcp_prev - cur_node.string_depth
            mid_node = break_edge(cur_node, s, edge_start, offset)
            cur_node = create_new_leaf(mid_node, s, suffix)
        if i < len(s) - 1:
            lcp_prev = lcp_array[i]
    return root

def print_tree(node):
    for c in sorted(node.children):
        child = node.children[c]
        print("%d %d" % (child.edge_start, child.edge_end + 1))
        print_tree(child)


def main():
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    root = stf_from_sa(text, sa, lcp)
    print_tree(root)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=main).start()