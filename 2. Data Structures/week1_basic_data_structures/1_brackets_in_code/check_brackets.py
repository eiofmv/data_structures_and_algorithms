# python3

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            if len(opening_brackets_stack) == 1:
                first_added = i
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i
            if not are_matching(opening_brackets_stack[-1], next):
                return i
            else:
                opening_brackets_stack.pop()
    if len(opening_brackets_stack) == 0:
        return -1
    else:
        return first_added


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1:
        print('Success')
    else:
        print(mismatch + 1)


if __name__ == "__main__":
    main()
