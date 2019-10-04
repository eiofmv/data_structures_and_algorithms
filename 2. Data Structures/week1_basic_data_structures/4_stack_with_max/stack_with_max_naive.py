#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_value = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__stack) == 1:
            self.__max_value = [a]
        else:
            self.__max_value.append(max(self.__max_value[-1], a))

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__max_value.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__max_value[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
