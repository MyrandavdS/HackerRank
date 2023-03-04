# player_1 = str(input())
# player_2 = str(input())
string = "BANANA"

player_1_count = 0
player_2_count = 0
#
# for i in range(len(string)):
#     if string[i] in "AEIOU":
#         index = (len(string) - i)
#         player_2_count += index
#         print("index : ", i)
#         print("vogal : ", player_2_count)
#         print(string[i:player_2_count])
#     else:
#         index = (len(string) - i)
#         player_1_count += index
#         print("index : ", i)
#         print("consonants : ", player_1_count)
#         print(string[i:player_1_count])
for i in range(len(string)):
    if string[i] in "AEIOU":
        player_2_count += (len(string) - i)
        print("player 2",string[i:player_2_count])
    else:
        player_1_count += (len(string) - i)
        print("player 1", string[i:player_1_count])
if player_2_count == player_1_count:
    print("Draw")
elif player_2_count > player_1_count:
    print("Kevin", player_2_count)
else:
    print("Stuart", player_1_count)
