string = input()
sub_string = input()

#def count_substring(string, sub_string):
# .find is to find the first index where the substring starts
#string_count = string.find(sub_string)
#total_string = int(string_count)
#print(string_count)
#print(total_string)
counter = 0

for i in range(len(string)):
    #print(string[i])
    if string[i: i+len(sub_string)] == sub_string:
        counter += 1
        #print(counter)
    print(counter)

def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if string[i: i+len(sub_string)] == sub_string:
            counter += 1
    return counter



