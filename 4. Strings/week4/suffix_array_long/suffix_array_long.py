# python3
import sys

def sort_characters(s):
  order = [0] * len(s)
  position = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
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
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # Implement this function yourself
  order = sort_characters(text)
  clas = compute_char_classes(text, order)
  l = 1
  while l < len(text):
    order = sort_doubled(text, l, order, clas)
    clas = update_classes(order, clas, l)
    l *= 2
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
