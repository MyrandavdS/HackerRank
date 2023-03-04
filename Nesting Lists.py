# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        sublist = []
        name = input()
        score = float(input())
        sublist.append(name)
        sublist.append(score)
        students.append(sublist)

    print(students)
    nextbig = 0
    pointer = 0
    biggest = 0
    egualStudents = []
    for i, c in enumerate(students):
        # print(i)
        print('current student to be compared', c)
        print('pointer is', pointer)
        position = i + 1
        if position < len(students):
            next = students[i + 1]

            if biggest == 0:
                biggest = c[1]
            else:
                biggest = students[pointer][1]
                print('bigger now is:', students[pointer][0], biggest)
            # comparing values
            print('is', students[pointer][0], 'bigger than', students[i + 1][0], '?')
            print('is', biggest, 'bigger than', next[1], '?')
            if biggest == next[1]:
                egualStudents.append(next[0])
                egualStudents.append(students[pointer][0])
            if biggest > next[1]:
                if biggest != students[pointer][1]:
                    pointer = i
                    biggest = students[i][1]
                    print('yes! bigger is current:', students[pointer][0])
            else:
                pointer = i + 1
                print('no! bigger is next:', students[pointer][0])

    print('winner', students[pointer][0])
    print('equals students', egualStudents)


