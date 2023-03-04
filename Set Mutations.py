set_a_input = int(input())
set_a_set = set(input().split())

other_sets = int(input())

for i in range(other_sets):
    operation = (input().split())
    inter_set = set(input().split())
    if inter_set.__len__() == int(operation[1]):
        if operation[0] == 'intersection_update':
            set_a_set.intersection_update(inter_set)
            print(set_a_set)
        if operation[0] == 'update':
            set_a_set.update(inter_set)
            print(set_a_set)
        if operation[0] == 'symmetric_difference_update':
            set_a_set.symmetric_difference_update(inter_set)
            print(set_a_set)
        if operation[0] == 'difference_update':
            set_a_set.difference_update(inter_set)
            print(set_a_set)

    #if operation[0] == 'intersection_update':

    #o = operation.replace('_',' ')
    #func = o.split()
    #print(func)
# map is making the list into an integer, list is making the set into a list
totlist = list(map(int, set_a_set))
print(totlist)
total = sum(totlist)
print(total)

#TestTestTest
