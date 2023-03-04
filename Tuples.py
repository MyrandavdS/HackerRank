# Tuples are immutable which means they cannot be modified once created
# This restricts their use because we cannot add, remove, or assign values
# Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashable.
# An object is hashable if it has a hash value which never changes during its lifetime
# A variabel kan je ook in een list, tuple etc maken door de benaming van wat je want ervoor te typen


if __name__ == '__main__':
    # t is een tuple () <- herkenbaar
    t = ()
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

