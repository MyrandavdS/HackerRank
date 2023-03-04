from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sub_string = string[i:i+k]
        answer = "".join(OrderedDict.fromkeys(sub_string))
        print(answer)
# An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)