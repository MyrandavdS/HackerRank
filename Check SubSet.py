test_cases = int(input())

for i in range(test_cases):

    set_a_input = int(input())
    set_a_set = set(input().split())
    set_b_input = int(input())
    set_b_set = set(input().split())



    print(set_a_set)
    print(set_b_set)

    subset = set_a_set.issubset(set_b_set)
    print(subset)




# for i in range(int(input())):
#     numbers = int(input())
#     case_set = input().split()
#
#     #if i[0]:
#         set_a.add(case_set)
#     #elif i[1]


