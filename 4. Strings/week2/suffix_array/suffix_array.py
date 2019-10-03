# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  array = []
  for i in range(len(text)):
    array.append((text[i:] + text[:i], i))

  array = sorted(array, key=lambda x: x[0])
  result = list(map(lambda x: x[1], array))

  # Implement this function yourself
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
