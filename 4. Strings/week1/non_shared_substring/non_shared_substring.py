# python3
import sys
import threading


def sort_characters(s):
    order = [0] * len(s)
    position = {'#': 0, '$': 1, 'A': 2, 'C': 3, 'G': 4, 'T': 5}
    count = [0] * len(position)
    for i in range(len(s)):
        count[position[s[i]]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(s))[::-1]:
        c = position[s[i]]
        count[c] -= 1
        order[count[c]] = i
    return order


def compute_char_classes(s, order):
    clas = [0] * len(s)
    clas[order[0]] = 0
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i - 1]]:
            clas[order[i]] = clas[order[i - 1]] + 1
        else:
            clas[order[i]] = clas[order[i - 1]]
    return clas


def sort_doubled(s, l, order, clas):
    count = [0] * len(s)
    new_order = [0] * len(s)
    for i in range(len(s)):
        count[clas[i]] += 1
    for i in range(1, len(s)):
        count[i] += count[i - 1]
    for i in range(len(s))[::-1]:
        start = (order[i] - l + len(s)) % len(s)
        cl = clas[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, clas, l):
    n = len(new_order)
    new_class = [0] * n
    new_class[new_order[0]] = 0
    for i in range(1, n):
     cur = new_order[i]
     prev = new_order[i - 1]
     mid = (cur + l) % n
     mid_prev = (prev + l) % n
     if clas[cur] != clas[prev] or clas[mid] != clas[mid_prev]:
       new_class[cur] = new_class[prev] + 1
     else:
       new_class[cur] = new_class[prev]
    return new_class


def build_suffix_array(text):
  order = sort_characters(text)
  clas = compute_char_classes(text, order)
  l = 1
  while l < len(text):
    order = sort_doubled(text, l, order, clas)
    clas = update_classes(order, clas, l)
    l *= 2
  return order


def lcp_of_suffixes(s, i, j, equal):
  lcp = max(0, equal)
  while (i + lcp < len(s)) and (j + lcp < len(s)):
    if s[i + lcp] == s[j + lcp]:
      lcp += 1
    else:
      break
  return lcp


def invert_suffix_array(order):
  pos = [0] * len(order)
  for i in range(len(pos)):
    pos[order[i]] = i
  return pos


def compute_lcp_array(s, order):
  lcp_array = [0] * (len(s) - 1)
  lcp = 0
  pos_id_order = invert_suffix_array(order)
  suffix = order[0]
  for i in range(len(s)):
    order_index = pos_id_order[suffix]
    if order_index == len(s) - 1:
      lcp = 0
      suffix = (suffix + 1) % len(s)
      continue
    next_suffix = order[order_index + 1]
    lcp = lcp_of_suffixes(s, suffix, next_suffix, lcp - 1)
    lcp_array[order_index] = lcp
    suffix = (suffix + 1) % len(s)
  return lcp_array


class SuffixTreeNode:
  def __init__(self, parent=None, children=None, string_depth=0, edge_start=-1, edge_end=-1):
    self.parent = parent
    self.children = children if children else {}
    self.string_depth = string_depth
    self.edge_start = edge_start
    self.edge_end = edge_end
    self.type = 'l'


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


def build_suffix_tree(text):
  sa = build_suffix_array(text)
  lcp = compute_lcp_array(text, sa)
  tree = stf_from_sa(text, sa, lcp)
  return tree


def find_r_leafs(tree, length):
    if len(tree.children) == 0:
        if tree.edge_start > length:
            tree.type = 'r'
    for child in tree.children:
        node = tree.children[child]
        find_r_leafs(node, length)


def find_min_substring(node, candidate):
  if len(node.children) == 0:
      if node.type == 'r':
          candidate[1] += 1
      if candidate[1] > node.edge_start + 1:
          candidate[1] = node.edge_start + 1

  for c in node.children:
    child = node.children[c]
    candidate = find_min_substring(child, candidate)

  return candidate


def solve (p, q):
  tree = build_suffix_tree(p + '#' + q + '$')
  find_r_leafs(tree, len(p))

  min_substring = (0, len(p))
  for child in tree.children:
    node = tree.children[child]
    start = node.edge_start

    if start < len(p):
      candidate = [start, start + len(p)]
      candidate = find_min_substring(node, candidate)

      if ((candidate[1] - candidate[0] < min_substring[1] - min_substring[0])and
              (candidate[1] - candidate[0] > 0)and(candidate[1] <= len(p))):
        min_substring = candidate

  return p[min_substring[0]:min_substring[1]]


def main():
  p = sys.stdin.readline().strip()
  q = sys.stdin.readline().strip()

  ans = solve (p, q)

  sys.stdout.write (ans + '\n')

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
