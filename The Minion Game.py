# player_1 = str(input())
# player_2 = str(input())
string = str(input())

player_1_count = 0
player_2_count = 0

for i in range(len(string)):
    if string[i] in "AEIOU":
        index = (len(string) - i)
        player_2_count += index
        # print("index : ", i)
        # print("vogal : ", player_2_count)
        print(string[i:player_2_count])
        # print(len(string) - i)
    else:
        index = (len(string) - i)
        player_1_count += index
        # print("index : ", i)
        # print("consonants : ", player_1_count)
        print(string[i:player_1_count])
        #print(i)
        #print(string[i])
        # print(string[i:index])
        # print(len(string) - i)

